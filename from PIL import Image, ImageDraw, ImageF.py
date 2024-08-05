from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Function to get team data
def get_team_data():
    teams = []
    for i in range(1, 6):  # Assuming you have 5 teams
        team_name = input(f"Enter the name of Team #{i}: ")
        placement = int(input(f"Enter the placement for {team_name} (1-5): "))
        kills = int(input(f"Enter the kill points for {team_name}: "))
        teams.append((team_name, placement, kills))
    return teams

# Function to calculate placement points
def calculate_placement_points(placement):
    if placement == 1:
        return 10
    elif placement == 2:
        return 6
    elif placement == 3:
        return 5
    elif placement == 4:
        return 4
    elif placement == 5:
        return 3
    else:
        return 0

# Create a dataframe from the team data and calculate total points
def create_point_table(teams):
    data = []
    for team in teams:
        team_name, placement, kills = team
        placement_points = calculate_placement_points(placement)
        kill_points = max(kills, 0)  # Ensure kill points are at least 0
        total_points = placement_points + kill_points
        data.append((team_name, placement, kills, placement_points, total_points))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Team', 'Placement', 'K', 'P', 'T'])
    
    # Calculate how many times each team was ranked 1st
    df['W'] = df['Placement'].apply(lambda x: 1 if x == 1 else 0)
    
    # Sort DataFrame by Total Points
    df = df.sort_values(by='T', ascending=False).reset_index(drop=True)
    
    # Add Rank Column
    df['#'] = df.index + 1
    
    # Reorder columns to the required format
    df = df[['#', 'Team', 'W', 'K', 'P', 'T']]
    
    return df

# Function to overlay text on the image
def overlay_text_on_image(image_path, output_path, df, coords):
    # Load the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Define font and size
    try:
        font = ImageFont.truetype("arialbd.ttf", 24)  # Use a bold font
    except IOError:
        font = ImageFont.load_default()
    
    # Add team names and points
    for i, row in df.iterrows():
        team_coords = coords[i]
        draw.text(team_coords, row['Team'], font=font, fill="white")  # White color for team names
        draw.text((team_coords[0] + 200, team_coords[1]), str(row['W']), font=font, fill="black")
        draw.text((team_coords[0] + 250, team_coords[1]), str(row['K']), font=font, fill="black")
        draw.text((team_coords[0] + 300, team_coords[1]), str(row['P']), font=font, fill="black")
        draw.text((team_coords[0] + 350, team_coords[1]), str(row['T']), font=font, fill="black")
    
    # Save the updated image
    img.save(output_path)
    print(f"Image saved as '{output_path}'.")

# Main function
def main():
    teams = get_team_data()
    point_table = create_point_table(teams)
    print("\nPoint Table:")
    print(point_table)
    
    # Coordinates for team names on the image
    coords = [
        (240, 491), (240, 560), (240, 630), (240, 700), 
        (240, 770), (240, 840), (240, 910), (240, 980), 
        (241, 1050), (241, 1120)
    ]
    
    # Overlay text on the image
    overlay_text_on_image('D:\Web\PT.png.png', 'updated_point_table.png', point_table, coords)

if __name__ == "__main__":
    main()
