"""
YouTube Video Downloader
- Select video quality
- Preview file size before download
- Choose download location
"""

import os
import sys

try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("yt-dlp is not installed. Installing now...")
    os.system(f"{sys.executable} -m pip install yt-dlp")
    from yt_dlp import YoutubeDL


def get_video_info(url: str) -> dict:
    """Fetch video information without downloading."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def format_size(bytes_size: int) -> str:
    """Convert bytes to human-readable format."""
    if bytes_size is None:
        return "Unknown"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"


def get_available_formats(info: dict) -> list:
    """Extract available video formats with quality info."""
    formats = []
    seen_resolutions = set()
    
    for f in info.get('formats', []):
        # Only include formats with video
        if f.get('vcodec') == 'none':
            continue
            
        resolution = f.get('resolution', 'N/A')
        height = f.get('height')
        ext = f.get('ext', 'mp4')
        filesize = f.get('filesize') or f.get('filesize_approx')
        format_id = f.get('format_id')
        fps = f.get('fps', '')
        
        # Create a unique key for resolution
        key = f"{height}p" if height else resolution
        
        if height and key not in seen_resolutions:
            seen_resolutions.add(key)
            formats.append({
                'format_id': format_id,
                'resolution': key,
                'height': height or 0,
                'ext': ext,
                'filesize': filesize,
                'fps': fps,
            })
    
    # Sort by resolution (height) descending
    formats.sort(key=lambda x: x['height'], reverse=True)
    return formats


def display_formats(formats: list) -> None:
    """Display available formats in a nice table."""
    print("\n" + "=" * 60)
    print("Available Video Qualities:")
    print("=" * 60)
    print(f"{'#':<4} {'Resolution':<12} {'Format':<8} {'FPS':<6} {'Size':<12}")
    print("-" * 60)
    
    for idx, fmt in enumerate(formats, 1):
        size_str = format_size(fmt['filesize'])
        fps_str = f"{fmt['fps']}fps" if fmt['fps'] else "N/A"
        print(f"{idx:<4} {fmt['resolution']:<12} {fmt['ext']:<8} {fps_str:<6} {size_str:<12}")
    
    print("=" * 60)


def get_download_location() -> str:
    """Prompt user for download location."""
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    print(f"\nDefault download location: {default_path}")
    custom_path = input("Enter custom download path (or press Enter for default): ").strip()
    
    if custom_path:
        # Expand user home directory if ~ is used
        custom_path = os.path.expanduser(custom_path)
        
        if not os.path.exists(custom_path):
            create = input(f"Directory '{custom_path}' doesn't exist. Create it? (y/n): ").strip().lower()
            if create == 'y':
                os.makedirs(custom_path, exist_ok=True)
                print(f"Created directory: {custom_path}")
            else:
                print("Using default location instead.")
                return default_path
        return custom_path
    
    return default_path


def download_video(url: str, format_id: str, download_path: str, title: str) -> None:
    """Download the video with selected format."""
    ydl_opts = {
        'format': f"{format_id}+bestaudio/best",
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [download_progress_hook],
    }
    
    print(f"\nDownloading: {title}")
    print(f"Saving to: {download_path}")
    print("-" * 40)
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("\n✅ Download completed successfully!")


def download_progress_hook(d):
    """Hook to display download progress."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rProgress: {percent} | Speed: {speed} | ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print("\nDownload finished, now processing...")


def main():
    print("=" * 60)
    print("       YouTube Video Downloader")
    print("=" * 60)
    
    # Get YouTube URL
    url = input("\nEnter YouTube video URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting.")
        return
    
    print("\n🔍 Fetching video information...")
    
    try:
        info = get_video_info(url)
    except Exception as e:
        print(f"❌ Error fetching video info: {e}")
        return
    
    title = info.get('title', 'Unknown')
    duration = info.get('duration', 0)
    uploader = info.get('uploader', 'Unknown')
    
    print(f"\n📹 Video: {title}")
    print(f"👤 Channel: {uploader}")
    print(f"⏱️  Duration: {duration // 60}:{duration % 60:02d}")
    
    # Get available formats
    formats = get_available_formats(info)
    
    if not formats:
        print("❌ No suitable video formats found.")
        return
    
    # Display available formats
    display_formats(formats)
    
    # Let user select quality
    while True:
        try:
            choice = input("\nSelect quality (enter number): ").strip()
            choice_idx = int(choice) - 1
            
            if 0 <= choice_idx < len(formats):
                selected_format = formats[choice_idx]
                break
            else:
                print("❌ Invalid selection. Please try again.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    # Show selected format details
    print(f"\n✅ Selected: {selected_format['resolution']} ({selected_format['ext']})")
    
    # Show file size and ask for confirmation
    size_str = format_size(selected_format['filesize'])
    print(f"📦 Estimated file size: {size_str}")
    
    # Get download location
    download_path = get_download_location()
    
    # Final confirmation
    print("\n" + "=" * 60)
    print("Download Summary:")
    print(f"  Video: {title}")
    print(f"  Quality: {selected_format['resolution']}")
    print(f"  Size: {size_str}")
    print(f"  Location: {download_path}")
    print("=" * 60)
    
    proceed = input("\n🚀 Proceed with download? (y/n): ").strip().lower()
    
    if proceed != 'y':
        print("❌ Download cancelled.")
        return
    
    # Download the video
    try:
        download_video(url, selected_format['format_id'], download_path, title)
    except Exception as e:
        print(f"\n❌ Error during download: {e}")
        return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Download cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
