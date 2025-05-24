import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, UnidentifiedImageError
from bs4 import BeautifulSoup
import cairosvg
import random
import numpy as np
from adding_15_features_modified import add_features_now
import time


# Function to add watermark to an image
def add_watermark_at_bottom_right(input_image_path, output_image_path, watermark_text):
    try:
        img = Image.open(input_image_path).convert("RGBA")
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {input_image_path}")
        return

    # Enhance brightness of alpha channel
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.8)
    img.putalpha(alpha)

    # Add text watermark at bottom right corner
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(watermark_text, font)
    width, height = img.size
    x = width - textwidth - 10
    y = height - textheight - 10

    # Apply the watermark text
    draw.text((x, y), watermark_text, font=font, fill=(220, 220, 220, 128))

    img = img.convert("RGB")
    img.save(output_image_path, "PNG")


# Function to add watermark diagonally
def add_watermark_diagonally(input_image_path, output_image_path, watermark_text):
    try:
        img = Image.open(input_image_path).convert("RGBA")
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {input_image_path}")
        return

    # Adding diagonal text watermark
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Calculate text size
    textwidth, textheight = draw.textsize(watermark_text, font)

    # Create a new image for the text
    text_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw_text = ImageDraw.Draw(text_img)

    # Calculate the position for the text
    width, height = img.size
    x = -width // 4  # Starting position (can be adjusted)
    y = height - textheight  # Start from the bottom

    # Draw text repeatedly across the image diagonally
    while y > -height:
        draw_text.text((x, y), watermark_text, font=font, fill=(220, 220, 220, 128))
        x += textwidth
        y -= textheight

    # Rotate the text image to cover from bottom left to top right
    text_img = text_img.rotate(35, expand=1)

    # Ensure the rotated image is the same size as the original
    text_img = text_img.resize(img.size, Image.ANTIALIAS)

    # Combine images
    img = Image.alpha_composite(img, text_img)

    img = img.convert("RGB")
    img.save(output_image_path, "PNG")


# Function to add rotation, brightness, and Gaussian blur
def add_rotation_brightness_gaussian_blur(input_image_path, output_image_path, watermark_text=None):
    try:
        img = Image.open(input_image_path).convert("RGBA")
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {input_image_path}")
        return

    # Apply random rotation
    angle = random.randint(-15, 15)
    img = img.rotate(angle, expand=True)

    # Apply random brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(random.uniform(0.25, 0.5))

    # # Apply Gaussian blur
    # img = img.filter(ImageFilter.GaussianBlur(radius=random.randint(0, 4)))

    img = img.convert("RGB")
    img.save(output_image_path, "PNG")


# Function to add rotation and grey-colored mesh
def add_rotation_grey_colored_mesh(input_image_path, output_image_path, watermark_text=None):
    try:
        img = Image.open(input_image_path).convert("RGBA")
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {input_image_path}")
        return

    width, height = img.size

    # Apply random rotation
    angle = random.randint(-15, 15)
    img = img.rotate(angle, expand=True)

    # Create a blank image with the same size and mode
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(overlay)

    # Set grid size and line color
    grid_size = 2  # Adjust as needed
    line_color = (128, 128, 128, 80)  # Grey color with transparency

    # Draw horizontal grid lines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)

    # Draw vertical grid lines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)

    # Composite the overlay onto the original image
    result = Image.alpha_composite(img, overlay)

    result = result.convert("RGB")
    result.save(output_image_path, "PNG")


# Function to add Gaussian noise and JPEG compression
def add_gaussian_noise_jpeg_compression(input_image_path, output_image_path, watermark_text=None):
    try:
        img = Image.open(input_image_path).convert("RGBA")
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {input_image_path}")
        return

    # Add Gaussian Noise to the image
    np_img = np.array(img)
    noise = np.random.normal(1, 0.5, np_img.shape)
    np_img = np.clip(np_img + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(np_img, 'RGBA')

    img = img.convert("RGB")
    img.save(output_image_path, "PNG")


# Function to handle SVG files
def handle_svg(input_svg_path, output_image_path, watermark_text):
    try:
        # Convert SVG to PNG
        png_temp_path = input_svg_path.replace(".svg", ".png")
        cairosvg.svg2png(url=input_svg_path, write_to=png_temp_path)

        function_to_call = random.choice([add_watermark_at_bottom_right, add_watermark_diagonally, add_rotation_brightness_gaussian_blur, add_rotation_grey_colored_mesh, add_gaussian_noise_jpeg_compression])

        # Add watermark to the converted PNG image
        function_to_call(png_temp_path, output_image_path, watermark_text)

        # Clean up the temporary PNG file
        os.remove(png_temp_path)
    except Exception as e:
        print(f"An error occurred while handling SVG: {e}")


# Main script logic

def update_html_image_sources(html_file_path, local_resources_folder):
    # Parse HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all image tags and update src
    for img_tag in soup.find_all('img'):
        src = img_tag.get('src')
        if src and src.endswith(('.png', '.svg')):
            base_name = os.path.basename(src)
            modified_name = base_name.split('.')[0] + '_modified.png'
            new_src = src.replace(base_name, modified_name)
            img_tag['src'] = new_src

    # Save the modified HTML file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))


def process_images(local_resources_folder):
    local_resources_folder_img = os.path.join(local_resources_folder, 'img')
    for root, _, files in os.walk(local_resources_folder_img):
        for filename in files:
            if filename.endswith('.png') or filename.endswith('.svg'):
                input_image_path = os.path.join(root, filename)
                output_image_path = os.path.join(root, filename.split('.')[0] + '_modified.png')

                if filename.endswith('.png'):
                    # Apply random transformation functions on PNG images
                    function_to_call = random.choice([add_watermark_at_bottom_right, add_watermark_diagonally, add_rotation_brightness_gaussian_blur, add_rotation_grey_colored_mesh, add_gaussian_noise_jpeg_compression])
                    function_to_call(input_image_path, output_image_path, watermark_text="PhishOracle")

                elif filename.endswith('.svg'):
                    # Handle SVG files
                    handle_svg(input_image_path, output_image_path, watermark_text="PhishOracle")


# Function to find the parent folder of 'local_resources' and the corresponding HTML file
def find_target_html_and_local_resources(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "local_resources" in [d.lower() for d in dirs]:
            parent_dir = root  # Directory that contains 'local_resources'
            local_resources_path = os.path.join(parent_dir, "local_resources")

            for html_file in ['index.html', 'main.html']:
                html_path = os.path.join(parent_dir, html_file)
                if os.path.isfile(html_path):
                    return html_path, local_resources_path
    return None, None


def add_logo_based_features(main_folder):
    processing_time = []

    for folder_name in os.listdir(main_folder):
        folder_path = os.path.join(main_folder, folder_name)
        if not os.path.isdir(folder_path):
            continue

        start_time = time.time()
        html_path, local_resources_path = find_target_html_and_local_resources(folder_path)

        if html_path and local_resources_path:
            modified_html_path = os.path.join(os.path.dirname(html_path), "phishing_webpage.html")
            shutil.copy(html_path, modified_html_path)
            print(f"Copied {html_path} to {modified_html_path}")

            process_images(local_resources_path)
            update_html_image_sources(modified_html_path, local_resources_path)

            print(f"Adding visual features to: {modified_html_path}")
            add_features_now(modified_html_path)

            end_time = time.time()
            processing_time.append(end_time - start_time)
        else:
            print(f"No HTML or resources found in {folder_path}")

    if processing_time:
        print(f"Average processing time per folder: {sum(processing_time) / len(processing_time):.2f} seconds")
    else:
        print("No folders were processed.")


if __name__ == '__main__':
    modified_file = add_logo_based_features()
    add_features_now(modified_file)

from adding_15_features_modified import FEATURE_FUNCTIONS_MAP, apply_selected_content_features

VISUAL_FEATURES = {
    'watermark_bottom_right': add_watermark_at_bottom_right,
    'watermark_diagonal': add_watermark_diagonally,
    'blur_rotate': add_rotation_brightness_gaussian_blur,
    'grey_mesh': add_rotation_grey_colored_mesh,
    'noise_jpeg': add_gaussian_noise_jpeg_compression
}

def extract_all_features(folder_path):
    visual_names = list(VISUAL_FEATURES.keys())
    content_names = list(FEATURE_FUNCTIONS_MAP.keys())
    return visual_names + content_names

def apply_features(main_folder, selected_features):
    print(f"Processing all subfolders in: {main_folder}")

    for folder_name in os.listdir(main_folder):
        folder_path = os.path.join(main_folder, folder_name)
        if not os.path.isdir(folder_path):
            continue

        html_path, local_resources_path = find_target_html_and_local_resources(folder_path)
        if not html_path or not local_resources_path:
            print(f"[SKIPPED] No HTML or local_resources found in {folder_path}")
            continue

        print(f"[PROCESSING] {folder_name}")

        # ✅ Save phishing page inside the same subfolder
        modified_html_path = os.path.join(folder_path, "phishing_webpage.html")
        shutil.copy(html_path, modified_html_path)

        img_folder = os.path.join(local_resources_path, "img")
        if os.path.isdir(img_folder):
            for img_root, _, files in os.walk(img_folder):
                for fname in files:
                    if fname.endswith('.png') or fname.endswith('.svg'):
                        img_path = os.path.join(img_root, fname)
                        out_path = os.path.join(img_root, fname.split('.')[0] + '_modified.png')
                        for feat in selected_features:
                            if feat in VISUAL_FEATURES:
                                VISUAL_FEATURES[feat](img_path, out_path, watermark_text="PhishOracle")
        else:
            print(f"[WARNING] No img folder found in {local_resources_path}")

        update_html_image_sources(modified_html_path, local_resources_path)

        content_feats = [f for f in selected_features if f in FEATURE_FUNCTIONS_MAP]
        apply_selected_content_features(modified_html_path, content_feats)

        print(f"[SUCCESS] phishing_webpage.html created in: {folder_path}")

    print("[DONE] All phishing pages generated.")
    return main_folder
