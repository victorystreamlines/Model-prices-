try:
    from PIL import Image, ImageDraw, ImageFont
    import base64
    import io
    
    # Create a 32x32 image for favicon
    size = 32
    img = Image.new('RGBA', (size, size), (15, 23, 42, 255))  # Dark blue background
    draw = ImageDraw.Draw(img)
    
    # Draw background circle
    draw.ellipse([2, 2, 30, 30], fill=(31, 78, 121, 255), outline=(0, 255, 255, 255), width=1)
    
    # Draw letter M in center
    try:
        # Try to use a system font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 18)
        except:
            font = ImageFont.load_default()
    
    # Draw the M letter
    draw.text((12, 6), "M", fill=(0, 255, 255, 255), font=font)
    
    # Draw small chart bars at bottom
    colors = [(59, 130, 246, 255), (249, 124, 22, 255), (0, 255, 255, 255), (138, 43, 226, 255)]
    for i, color in enumerate(colors):
        x_pos = 8 + i * 4
        height = 4 + (i % 3)
        draw.rectangle([x_pos, 26-height, x_pos+2, 26], fill=color)
    
    # Save as PNG
    img.save('favicon.png')
    print("Generated favicon.png successfully!")
    
    # Convert to ICO format
    # Create different sizes for ICO
    sizes = [16, 32]
    images = []
    for s in sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        images.append(resized)
    
    # Save as ICO
    images[0].save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32)])
    print("Generated favicon.ico successfully!")
    
except ImportError:
    print("PIL not available, creating a simple favicon...")
    # Create a simple text-based favicon
    with open('favicon.ico', 'w') as f:
        f.write("")  # Empty file as fallback
    print("Created empty favicon.ico as fallback")
