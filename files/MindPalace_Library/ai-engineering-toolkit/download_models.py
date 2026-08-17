#!/usr/bin/env python3
"""
Model downloader for AI Engineering Toolkit.
Downloads all required models for the 2x H200 setup.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

MODEL_DIR = Path("models")

# Model definitions: (url, destination, description)
MODELS = [
    # Pony Diffusion V6 XL (NSFW, SDXL)
    (
        "https://civitai.com/api/download/models/290640?fileId=228616",
        MODEL_DIR / "checkpoints" / "v6.safetensors",
        "Pony Diffusion V6 XL (6.46 GB)"
    ),
    # SDXL VAE
    (
        "https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/ae.safetensors",
        MODEL_DIR / "vae" / "sdxl_vae.safetensors",
        "SDXL VAE (335 MB)"
    ),
    # FLUX.1 Dev
    (
        "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors",
        MODEL_DIR / "unet" / "flux1-dev.safetensors",
        "FLUX.1 Dev (23.8 GB)"
    ),
    # FLUX.1 VAE
    (
        "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors",
        MODEL_DIR / "vae" / "ae.safetensors",
        "FLUX VAE (335 MB)"
    ),
    # CLIP-L for FLUX
    (
        "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors",
        MODEL_DIR / "clip" / "clip_l.safetensors",
        "CLIP-L Text Encoder (246 MB)"
    ),
    # T5-XXL FP8 for FLUX
    (
        "https://huggingface.co/comfyanonymous/t5xxl_fp8_e4m3fn/resolve/main/t5xxl_fp8_e4m3fn.safetensors",
        MODEL_DIR / "clip" / "t5xxl_fp8_e4m3fn.safetensors",
        "T5-XXL FP8 Text Encoder (4.89 GB)"
    ),
    # Abliterated T5 for FLUX.1 Dev (NSFW)
    (
        "https://huggingface.co/aoxo/flux.1dev-abliterated/resolve/main/text_encoder/model.safetensors",
        MODEL_DIR / "clip" / "t5xxl_fp8_abliterated.safetensors",
        "Abliterated T5-XXL FP8 (4.89 GB)"
    ),
    # FLUX.2 Klein 9B FP8
    (
        "https://huggingface.co/Aitrepreneur/FLX/resolve/main/flux-2-klein-9b-fp8.safetensors",
        MODEL_DIR / "unet" / "flux-2-klein-9b-fp8.safetensors",
        "FLUX.2 Klein 9B FP8 (8.79 GB)"
    ),
    # Abliterated Qwen3 TE for FLUX.2 Klein
    (
        "https://huggingface.co/ponpoke/flux2-klein-9b-uncensored-text-encoder/resolve/main/model.safetensors",
        MODEL_DIR / "clip" / "qwen3_abliterated.safetensors",
        "Abliterated Qwen3 Text Encoder (4.89 GB)"
    ),
    # Wan 2.2 14B NSFW (Phr00t Rapid AIO Q5_K)
    (
        "https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/v10/wan2.2-t2v-rapid-aio-v10-nsfw-Q5_K.gguf",
        MODEL_DIR / "diffusion_models" / "wan2.2-t2v-rapid-aio-v10-nsfw-Q5_K.gguf",
        "Wan 2.2 14B NSFW Q5_K (GGUF)"
    ),
    # Wan 2.2 VAE
    (
        "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors",
        MODEL_DIR / "vae" / "wan_2.1_vae.safetensors",
        "Wan 2.1/2.2 VAE (254 MB)"
    ),
    # UMT5-XXL Encoder Q3_K_M for Wan
    (
        "https://huggingface.co/city96/umt5-xxl-encoder-gguf/resolve/main/umt5-xxl-encoder-Q3_K_M.gguf",
        MODEL_DIR / "clip" / "umt5-xxl-encoder-Q3_K_M.gguf",
        "UMT5-XXL Encoder Q3_K_M (3 GB)"
    ),
    # LTX-Video 2.3 Distilled 2B
    (
        "https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-2b-distilled.safetensors",
        MODEL_DIR / "diffusion_models" / "ltx-2.3-2b-distilled.safetensors",
        "LTX-Video 2.3 Distilled 2B"
    ),
    # LTX-Video 2.3 Text Projection
    (
        "https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/text_encoders/ltx-2.3_text_projection_bf16.safetensors",
        MODEL_DIR / "text_encoders" / "ltx-2.3_text_projection_bf16.safetensors",
        "LTX 2.3 Text Projection"
    ),
    # LTX-Video 2.3 Video VAE
    (
        "https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/vae/LTX23_video_vae_bf16.safetensors",
        MODEL_DIR / "vae" / "LTX23_video_vae_bf16.safetensors",
        "LTX 2.3 Video VAE"
    ),
    # LTX-Video 2.3 Audio VAE
    (
        "https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/vae/LTX23_audio_vae_bf16.safetensors",
        MODEL_DIR / "vae" / "LTX23_audio_vae_bf16.safetensors",
        "LTX 2.3 Audio VAE"
    ),
]


def ensure_dirs():
    """Create all necessary model directories."""
    dirs = [
        "checkpoints", "unet", "diffusion_models", "vae",
        "clip", "text_encoders", "loras", "clip_vision"
    ]
    for d in dirs:
        (MODEL_DIR / d).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created model directories in {MODEL_DIR}")


def download_file(url: str, dest: Path, description: str) -> bool:
    """Download a file using wget with resume support."""
    if dest.exists():
        print(f"✓ Already exists: {dest.name}")
        return True

    print(f"⬇ Downloading: {description}")
    print(f"   From: {url}")
    print(f"   To:   {dest}")

    try:
        # Use wget with resume support
        result = subprocess.run([
            "wget", "-c", "--progress=bar:force",
            "-O", str(dest), url
        ], check=True, capture_output=False)
        print(f"✓ Downloaded: {dest.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to download {description}: {e}")
        if dest.exists():
            dest.unlink()  # Remove partial download
        return False
    except FileNotFoundError:
        print("✗ wget not found. Please install wget or use aria2c.")
        return False


def main():
    print("=" * 60)
    print("AI Engineering Toolkit - Model Downloader")
    print("=" * 60)

    ensure_dirs()

    print(f"\nDownloading {len(MODELS)} models...\n")

    success = 0
    failed = 0

    for url, dest, description in MODELS:
        if download_file(url, dest, description):
            success += 1
        else:
            failed += 1
        print()  # Empty line between downloads

    print("=" * 60)
    print(f"Download complete: {success} succeeded, {failed} failed")
    print("=" * 60)

    if failed > 0:
        print("\n⚠ Some downloads failed. You may need to:")
        print("  1. Accept licenses on HuggingFace/CivitAI for gated models")
        print("  2. Set HF_TOKEN environment variable")
        print("  3. Manually download failed models")
        sys.exit(1)

    print("\n✓ All models downloaded successfully!")
    print("\nNext steps:")
    print("  1. Accept model licenses on HuggingFace/CivitAI")
    print("  2. Run: docker-compose up -d")
    print("  3. Access ComfyUI at http://localhost:8188 (GPU 0) and http://localhost:8189 (GPU 1)")


if __name__ == "__main__":
    main()