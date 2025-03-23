from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename, color):
    # Create a new image with a white background
    image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a shield shape
    margin = size // 8
    shield_width = size - (2 * margin)
    shield_height = size - (2 * margin)
    
    # Shield points
    points = [
        (margin, margin),  # Top left
        (margin + shield_width, margin),  # Top right
        (margin + shield_width, margin + (shield_height * 0.7)),  # Right middle
        (margin + (shield_width / 2), margin + shield_height),  # Bottom middle
        (margin, margin + (shield_height * 0.7)),  # Left middle
    ]
    
    # Draw shield outline
    draw.polygon(points, fill=color)
    
    # Draw checkmark or X based on color
    if color == (40, 167, 69):  # Green/safe
        # Draw checkmark
        check_points = [
            (margin + (shield_width * 0.2), margin + (shield_height * 0.5)),
            (margin + (shield_width * 0.4), margin + (shield_height * 0.7)),
            (margin + (shield_width * 0.8), margin + (shield_height * 0.3))
        ]
        draw.line(check_points, fill='white', width=size//8)
    elif color == (220, 53, 69):  # Red/unsafe
        # Draw X
        margin_x = margin + (shield_width * 0.25)
        size_x = shield_width * 0.5
        draw.line(
            [(margin_x, margin_x), 
             (margin_x + size_x, margin_x + size_x)],
            fill='white', width=size//8
        )
        draw.line(
            [(margin_x + size_x, margin_x),
             (margin_x, margin_x + size_x)],
            fill='white', width=size//8
        )
    elif color == (0, 123, 255):  # Blue/loading
        # Draw dots for loading
        dot_size = size // 12
        center_x = margin + (shield_width / 2)
        center_y = margin + (shield_height / 2)
        dot_distance = size // 6
        
        for i in range(3):
            x = center_x + (i - 1) * dot_distance
            draw.ellipse(
                [x - dot_size, center_y - dot_size,
                 x + dot_size, center_y + dot_size],
                fill='white'
            )
    else:  # Error
        # Draw exclamation mark
        center_x = margin + (shield_width / 2)
        top_y = margin + (shield_height * 0.25)
        bottom_y = margin + (shield_height * 0.75)
        dot_y = margin + (shield_height * 0.85)
        
        # Exclamation line
        draw.rectangle(
            [center_x - size//16, top_y,
             center_x + size//16, bottom_y],
            fill='white'
        )
        # Dot
        draw.ellipse(
            [center_x - size//16, dot_y,
             center_x + size//16, dot_y + size//8],
            fill='white'
        )
    
    # Save the image
    image.save(filename)

def generate_all_icons():
    extension_dir = os.path.join(os.path.dirname(__file__), 'extension')
    
    # Create icons for different states
    icons = {
        'safe.png': (40, 167, 69),      # Green
        'unsafe.png': (220, 53, 69),    # Red
        'loading.png': (0, 123, 255),   # Blue
        'error.png': (108, 117, 125)    # Gray
    }
    
    # Generate icons for different sizes
    sizes = [16, 32, 48, 128]
    
    for icon_name, color in icons.items():
        # Standard icons
        create_icon(48, os.path.join(extension_dir, icon_name), color)
        
        # Extension manifest icons
        if icon_name == 'safe.png':  # Use safe icon as default extension icon
            for size in sizes:
                create_icon(
                    size,
                    os.path.join(extension_dir, f'icon{size}.png'),
                    color
                )

if __name__ == '__main__':
    generate_all_icons()
