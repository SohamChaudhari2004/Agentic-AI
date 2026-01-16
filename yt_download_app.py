"""
YouTube Video Downloader - Streamlit App
Features:
- Download videos in various qualities
- Download audio only (MP3)
- Download subtitles/captions
- Download thumbnails
- Preview video information
- Playlist support
"""

import os
import sys
import streamlit as st
from pathlib import Path

try:
    from yt_dlp import YoutubeDL
except ImportError:
    os.system(f"{sys.executable} -m pip install yt-dlp")
    from yt_dlp import YoutubeDL

# Page configuration
st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF0000;
        text-align: center;
        margin-bottom: 2rem;
    }
    .video-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1f1f1f;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
    }
    .stProgress > div > div > div > div {
        background-color: #FF0000;
    }
</style>
""", unsafe_allow_html=True)


# ============ Helper Functions ============

def format_size(bytes_size: int) -> str:
    """Convert bytes to human-readable format."""
    if bytes_size is None:
        return "Unknown"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"


def format_duration(seconds: int) -> str:
    """Convert seconds to HH:MM:SS format."""
    if not seconds:
        return "Unknown"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


@st.cache_data(ttl=300)
def get_video_info(url: str) -> dict:
    """Fetch video information without downloading."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def get_available_formats(info: dict) -> list:
    """Extract available video formats with quality info."""
    formats = []
    seen_resolutions = set()
    
    for f in info.get('formats', []):
        if f.get('vcodec') == 'none':
            continue
            
        height = f.get('height')
        ext = f.get('ext', 'mp4')
        filesize = f.get('filesize') or f.get('filesize_approx')
        format_id = f.get('format_id')
        fps = f.get('fps', '')
        
        key = f"{height}p" if height else None
        
        if height and key not in seen_resolutions:
            seen_resolutions.add(key)
            formats.append({
                'format_id': format_id,
                'resolution': key,
                'height': height or 0,
                'ext': ext,
                'filesize': filesize,
                'fps': fps,
                'display': f"{key} ({ext}) - {format_size(filesize)}"
            })
    
    formats.sort(key=lambda x: x['height'], reverse=True)
    return formats


def get_audio_formats(info: dict) -> list:
    """Extract available audio-only formats."""
    formats = []
    seen_bitrates = set()
    
    for f in info.get('formats', []):
        if f.get('vcodec') != 'none':
            continue
        if f.get('acodec') == 'none':
            continue
            
        abr = f.get('abr', 0)
        ext = f.get('ext', 'mp3')
        filesize = f.get('filesize') or f.get('filesize_approx')
        format_id = f.get('format_id')
        
        if abr and abr not in seen_bitrates:
            seen_bitrates.add(abr)
            formats.append({
                'format_id': format_id,
                'bitrate': abr,
                'ext': ext,
                'filesize': filesize,
                'display': f"{int(abr)}kbps ({ext}) - {format_size(filesize)}"
            })
    
    formats.sort(key=lambda x: x['bitrate'], reverse=True)
    return formats


def get_subtitles(info: dict) -> dict:
    """Extract available subtitles."""
    subtitles = info.get('subtitles', {})
    auto_captions = info.get('automatic_captions', {})
    
    return {
        'manual': subtitles,
        'auto': auto_captions
    }


def download_video(url: str, format_id: str, download_path: str, progress_bar, status_text) -> str:
    """Download video with selected format."""
    
    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                progress = downloaded / total
                progress_bar.progress(progress)
                status_text.text(f"Downloading: {progress*100:.1f}% | Speed: {d.get('_speed_str', 'N/A')} | ETA: {d.get('_eta_str', 'N/A')}")
        elif d['status'] == 'finished':
            status_text.text("Processing downloaded file...")
    
    ydl_opts = {
        'format': f"{format_id}+bestaudio/best",
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
        'quiet': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        
    return filename


def download_audio(url: str, download_path: str, audio_format: str, progress_bar, status_text) -> str:
    """Download audio only."""
    
    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                progress = downloaded / total
                progress_bar.progress(progress)
                status_text.text(f"Downloading: {progress*100:.1f}% | Speed: {d.get('_speed_str', 'N/A')}")
        elif d['status'] == 'finished':
            status_text.text("Converting to audio...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook],
        'quiet': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        
    return filename


def download_subtitles(url: str, download_path: str, languages: list, auto_subs: bool) -> list:
    """Download subtitles for the video."""
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': auto_subs,
        'subtitleslangs': languages,
        'subtitlesformat': 'srt',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'quiet': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
    return info.get('requested_subtitles', {})


def download_thumbnail(url: str, download_path: str) -> str:
    """Download video thumbnail."""
    ydl_opts = {
        'skip_download': True,
        'writethumbnail': True,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'quiet': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
    return info.get('thumbnail', '')


def get_playlist_info(url: str) -> dict:
    """Get playlist information."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'playlistend': 50,  # Limit to first 50 videos
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
    return info


# ============ Streamlit UI ============

def main():
    # Header
    st.markdown('<h1 class="main-header">📺 YouTube Downloader</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Download location
        default_path = str(Path.home() / "Downloads")
        download_path = st.text_input(
            "📁 Download Location",
            value=default_path,
            help="Enter the folder path where files will be saved"
        )
        
        # Create directory if it doesn't exist
        if download_path and not os.path.exists(download_path):
            if st.button("Create Directory"):
                os.makedirs(download_path, exist_ok=True)
                st.success(f"Created: {download_path}")
        
        st.divider()
        
        # Download mode
        download_mode = st.radio(
            "🎯 Download Mode",
            ["Video", "Audio Only", "Subtitles", "Thumbnail", "Playlist"],
            help="Choose what you want to download"
        )
        
        if download_mode == "Audio Only":
            audio_format = st.selectbox(
                "🎵 Audio Format",
                ["mp3", "m4a", "wav", "flac", "aac"],
                help="Choose audio output format"
            )
        else:
            audio_format = "mp3"
        
        st.divider()
        
        st.markdown("### 📋 Features")
        st.markdown("""
        - ✅ Video download (multiple qualities)
        - ✅ Audio extraction (MP3, etc.)
        - ✅ Subtitle download
        - ✅ Thumbnail download
        - ✅ Playlist support
        - ✅ File size preview
        """)
    
    # Main content
    url = st.text_input(
        "🔗 Enter YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste a YouTube video or playlist URL"
    )
    
    if url:
        try:
            with st.spinner("🔍 Fetching video information..."):
                if download_mode == "Playlist" and ("playlist" in url.lower() or "list=" in url):
                    info = get_playlist_info(url)
                    is_playlist = True
                else:
                    info = get_video_info(url)
                    is_playlist = False
            
            if is_playlist and info.get('_type') == 'playlist':
                # Playlist mode
                st.success(f"📋 Playlist: {info.get('title', 'Unknown')}")
                
                entries = info.get('entries', [])
                st.info(f"Found {len(entries)} videos in playlist")
                
                # Display playlist videos
                with st.expander("📜 Videos in Playlist", expanded=True):
                    for idx, entry in enumerate(entries, 1):
                        st.write(f"{idx}. {entry.get('title', 'Unknown')}")
                
                if st.button("⬇️ Download All (Best Quality)", type="primary"):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for idx, entry in enumerate(entries):
                        status_text.text(f"Downloading {idx+1}/{len(entries)}: {entry.get('title', 'Unknown')}")
                        try:
                            video_url = f"https://www.youtube.com/watch?v={entry.get('id')}"
                            ydl_opts = {
                                'format': 'bestvideo+bestaudio/best',
                                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                                'merge_output_format': 'mp4',
                                'quiet': True,
                            }
                            with YoutubeDL(ydl_opts) as ydl:
                                ydl.download([video_url])
                        except Exception as e:
                            st.warning(f"Failed to download: {entry.get('title')} - {e}")
                        
                        progress_bar.progress((idx + 1) / len(entries))
                    
                    st.success("✅ Playlist download completed!")
                    st.balloons()
            
            else:
                # Single video mode
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    # Thumbnail
                    thumbnail = info.get('thumbnail')
                    if thumbnail:
                        st.image(thumbnail, use_container_width=True)
                
                with col2:
                    # Video info
                    st.markdown(f"### {info.get('title', 'Unknown')}")
                    
                    info_col1, info_col2, info_col3 = st.columns(3)
                    
                    with info_col1:
                        st.metric("👤 Channel", info.get('uploader', 'Unknown'))
                    with info_col2:
                        st.metric("⏱️ Duration", format_duration(info.get('duration', 0)))
                    with info_col3:
                        views = info.get('view_count', 0)
                        st.metric("👁️ Views", f"{views:,}" if views else "Unknown")
                
                st.divider()
                
                # Download options based on mode
                if download_mode == "Video":
                    formats = get_available_formats(info)
                    
                    if formats:
                        selected_format = st.selectbox(
                            "🎬 Select Video Quality",
                            options=range(len(formats)),
                            format_func=lambda x: formats[x]['display']
                        )
                        
                        fmt = formats[selected_format]
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.info(f"📐 Resolution: {fmt['resolution']}")
                        with col2:
                            st.info(f"📦 Size: {format_size(fmt['filesize'])}")
                        with col3:
                            st.info(f"🎞️ FPS: {fmt['fps'] or 'N/A'}")
                        
                        if st.button("⬇️ Download Video", type="primary", use_container_width=True):
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            try:
                                filename = download_video(
                                    url, fmt['format_id'], download_path,
                                    progress_bar, status_text
                                )
                                progress_bar.progress(1.0)
                                st.success(f"✅ Downloaded successfully!")
                                st.info(f"📁 Saved to: {download_path}")
                                st.balloons()
                            except Exception as e:
                                st.error(f"❌ Download failed: {e}")
                    else:
                        st.warning("No suitable video formats found.")
                
                elif download_mode == "Audio Only":
                    audio_formats = get_audio_formats(info)
                    
                    st.info(f"🎵 Will convert to: {audio_format.upper()}")
                    
                    if audio_formats:
                        st.write("Available audio qualities:")
                        for af in audio_formats[:5]:
                            st.write(f"  • {af['display']}")
                    
                    if st.button("⬇️ Download Audio", type="primary", use_container_width=True):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        try:
                            filename = download_audio(
                                url, download_path, audio_format,
                                progress_bar, status_text
                            )
                            progress_bar.progress(1.0)
                            st.success(f"✅ Audio downloaded successfully!")
                            st.info(f"📁 Saved to: {download_path}")
                            st.balloons()
                        except Exception as e:
                            st.error(f"❌ Download failed: {e}")
                
                elif download_mode == "Subtitles":
                    subs = get_subtitles(info)
                    manual_subs = subs.get('manual', {})
                    auto_subs = subs.get('auto', {})
                    
                    st.write("**Available Subtitles:**")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write("📝 Manual Subtitles:")
                        if manual_subs:
                            for lang in list(manual_subs.keys())[:10]:
                                st.write(f"  • {lang}")
                        else:
                            st.write("  None available")
                    
                    with col2:
                        st.write("🤖 Auto-generated:")
                        if auto_subs:
                            for lang in list(auto_subs.keys())[:10]:
                                st.write(f"  • {lang}")
                        else:
                            st.write("  None available")
                    
                    sub_language = st.text_input(
                        "Enter language code (e.g., 'en', 'es', 'fr')",
                        value="en"
                    )
                    use_auto = st.checkbox("Include auto-generated subtitles", value=True)
                    
                    if st.button("⬇️ Download Subtitles", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Downloading subtitles..."):
                                download_subtitles(url, download_path, [sub_language], use_auto)
                            st.success("✅ Subtitles downloaded!")
                            st.info(f"📁 Saved to: {download_path}")
                        except Exception as e:
                            st.error(f"❌ Download failed: {e}")
                
                elif download_mode == "Thumbnail":
                    thumbnail = info.get('thumbnail')
                    if thumbnail:
                        st.image(thumbnail, caption="Video Thumbnail", use_container_width=True)
                        
                        if st.button("⬇️ Download Thumbnail", type="primary", use_container_width=True):
                            try:
                                with st.spinner("Downloading thumbnail..."):
                                    download_thumbnail(url, download_path)
                                st.success("✅ Thumbnail downloaded!")
                                st.info(f"📁 Saved to: {download_path}")
                            except Exception as e:
                                st.error(f"❌ Download failed: {e}")
                    else:
                        st.warning("No thumbnail available for this video.")
                
                # Additional video metadata
                with st.expander("📊 Video Metadata"):
                    meta_col1, meta_col2 = st.columns(2)
                    
                    with meta_col1:
                        st.write(f"**Video ID:** {info.get('id', 'N/A')}")
                        st.write(f"**Upload Date:** {info.get('upload_date', 'N/A')}")
                        st.write(f"**Categories:** {', '.join(info.get('categories', ['N/A']))}")
                        st.write(f"**Age Limit:** {info.get('age_limit', 0)}")
                    
                    with meta_col2:
                        st.write(f"**Like Count:** {info.get('like_count', 'N/A'):,}" if info.get('like_count') else "**Like Count:** N/A")
                        st.write(f"**Comment Count:** {info.get('comment_count', 'N/A'):,}" if info.get('comment_count') else "**Comment Count:** N/A")
                        st.write(f"**Channel ID:** {info.get('channel_id', 'N/A')}")
                        st.write(f"**Live Status:** {'🔴 Live' if info.get('is_live') else '📹 Recorded'}")
                    
                    # Description
                    description = info.get('description', '')
                    if description:
                        st.write("**Description:**")
                        st.text_area("", value=description[:1000] + "..." if len(description) > 1000 else description, height=150, disabled=True)
                    
                    # Tags
                    tags = info.get('tags', [])
                    if tags:
                        st.write("**Tags:**")
                        st.write(", ".join(tags[:20]))
        
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("Please check if the URL is valid and try again.")
    
    else:
        # Welcome message
        st.info("👆 Enter a YouTube URL above to get started!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🎬 Video Download
            - Multiple quality options
            - Preview file size
            - MP4 output format
            """)
        
        with col2:
            st.markdown("""
            ### 🎵 Audio Extraction
            - MP3, M4A, WAV, FLAC
            - Best quality audio
            - Fast conversion
            """)
        
        with col3:
            st.markdown("""
            ### 📋 Playlist Support
            - Download entire playlists
            - Batch processing
            - Progress tracking
            """)


if __name__ == "__main__":
    main()
