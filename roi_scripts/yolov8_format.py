def polygon_to_bbox(roi_points):
    """Convert polygon ROI to YOLO bbox format"""
    # Extract all X and Y coordinates
    x_coords = [roi_points['TL_X'], roi_points['TR_X'], roi_points['BR_X'], roi_points['BL_X']]
    y_coords = [roi_points['TL_Y'], roi_points['TR_Y'], roi_points['BR_Y'], roi_points['BL_Y']]
    
    # Get bounding box
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    
    # Calculate YOLO format
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min
    
    return x_center, y_center, width, height

# Example usage
roi = {
    'TL_X': 0.3703, 'TL_Y': 0.4875,
    'TR_X': 0.4891, 'TR_Y': 0.4922,
    'BR_X': 0.4531, 'BR_Y': 0.9859,
    'BL_X': 0.0078, 'BL_Y': 0.9922
}

x_c, y_c, w, h = polygon_to_bbox(roi)
print(f"YOLO format: {x_c:.4f} {y_c:.4f} {w:.4f} {h:.4f}")
# Output: 0.2594 0.7633 0.4625 0.4672