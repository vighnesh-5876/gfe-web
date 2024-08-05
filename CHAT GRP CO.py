from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Function to get team data
def get_team_data():
    teams = []
    for i in range(1, 21):
        team_name = input(f"Enter the name of Team #{i}: ")
        while True:
            try:
                placement = int(input(f"Enter the placement for {team_name} (1-20): "))
                if placement < 1 or placement > 20:
                    raise ValueError("Placement must be between 1 and 20.")
                break
            except ValueError as e:
                print(e)
                continue
        while True:
            try:
                kills = int(input(f"Enter the kill points for {team_name}: "))
                if kills < 0:
                    raise ValueError("Kills must be a non-negative integer.")
                break
            except ValueError as e:
                print(e)
                continue
        teams.append((team_name, placement, kills))
    return teams

# Function to calculate placement points
def calculate_placement_points(placement):
    points = {1: 10, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1}
    return points.get(placement, 0)

# Create a dataframe from the team data and calculate total points
def create_point_table(teams):
    data = []
    for team in teams:
        team_name, placement, kills = team
        placement_points = calculate_placement_points(placement)
        kill_points = max(kills, 0)
        total_points = placement_points + kill_points
        data.append((team_name, placement, kills, placement_points, total_points))
    
    df = pd.DataFrame(data, columns=['Team', 'Placement', 'K', 'P', 'T'])
    df['W'] = df['Placement'].apply(lambda x: 1 if x == 1 else 0)
    df = df.sort_values(by='T', ascending=False).reset_index(drop=True)
    df['#'] = df.index + 1
    df = df[['#', 'Team', 'W', 'K', 'P', 'T']]
    return df

# Function to overlay text on the image
def overlay_text_on_image(image_path, output_path, df):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Define font and size
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Adjust size as needed
    except IOError:
        font = ImageFont.load_default()

    # Coordinates
    coordinates = {
        "Team Name": [(240, y) for y in range(491, 1821, 69)],
        "Kill Points": [(580, y) for y in range(491, 1821, 69)],
        "Total Points": [(900, y) for y in range(491, 1821, 69)],
        "Placement Points": [(1200, y) for y in range(491, 1821, 69)],
        "Win Time": [(680, y) for y in range(491, 1821, 69)],
    }

    # Draw team names, kill points, total points, placement points, and win time
    for i, row in df.iterrows():
        draw.text(coordinates["Team Name"][i], row['Team'], font=font, fill="white")
        draw.text(coordinates["Kill Points"][i], str(row['K']), font=font, fill="white")
        draw.text(coordinates["Total Points"][i], str(row['T']), font=font, fill="white")
        draw.text(coordinates["Placement Points"][i], str(row['P']), font=font, fill="white")
        draw.text(coordinates["Win Time"][i], str(row['W']), font=font, fill="white")

    # Save the updated image
    img.save(output_path)
    print(f"Image saved as '{output_path}'.")

# Main function
def main():
    teams = get_team_data()
    point_table = create_point_table(teams)
    print("\nPoint Table:")
    print(point_table)
    overlay_text_on_image('D:/Web/Untitled design.png', 'updated_point_table.png', point_table)

if __name__ == "__main__":
    main()
