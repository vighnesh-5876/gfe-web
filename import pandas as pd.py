import pandas as pd

# Function to get team data
def get_team_data():
    teams = []
    for i in range(1, 21):  # Updated to handle 20 teams
        team_name = input(f"Enter the name of Team #{i}: ")
        placement_match1 = int(input(f"Enter the placement for {team_name} in Match 1 (1-20): "))
        kills_match1 = int(input(f"Enter the kill points for {team_name} in Match 1: "))
        placement_match2 = int(input(f"Enter the placement for {team_name} in Match 2 (1-20): "))
        kills_match2 = int(input(f"Enter the kill points for {team_name} in Match 2: "))
        teams.append((team_name, placement_match1, kills_match1, placement_match2, kills_match2))
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
    elif placement == 6:
        return 2
    elif placement in [7, 8]:
        return 1
    else:
        return 0

# Create a dataframe from the team data and calculate total points
def create_point_table(teams):
    data = []
    for team in teams:
        team_name, placement1, kills1, placement2, kills2 = team
        placement_points1 = calculate_placement_points(placement1)
        kill_points1 = max(kills1, 0)  # Ensure kill points are at least 0
        total_points1 = placement_points1 + kill_points1
        
        placement_points2 = calculate_placement_points(placement2)
        kill_points2 = max(kills2, 0)  # Ensure kill points are at least 0
        total_points2 = placement_points2 + kill_points2

        total_points = total_points1 + total_points2
        total_kills = kills1 + kills2
        total_placements = placement_points1 + placement_points2
        
        data.append((team_name, placement1, kills1, placement2, kills2, total_points1, total_points2, total_kills, total_placements, total_points))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Team', 'Placement_Match1', 'K_Match1', 'Placement_Match2', 'K_Match2', 'P_Match1', 'P_Match2', 'K', 'P', 'T'])
    
    # Calculate how many times each team was ranked 1st
    df['W'] = (df['Placement_Match1'] == 1).astype(int) + (df['Placement_Match2'] == 1).astype(int)
    
    # Sort DataFrame by Total Points
    df = df.sort_values(by='T', ascending=False).reset_index(drop=True)
    
    # Add Rank Column
    df['#'] = df.index + 1
    
    # Reorder columns to the required format
    df = df[['#', 'Team', 'W', 'K', 'P', 'T']]
    
    return df

# Function to export to Excel with formatting
def export_to_excel(df, filename):
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Point Table')
        
        workbook  = writer.book
        worksheet = writer.sheets['Point Table']
        
        # Set column widths
        column_widths = [5, 20, 15, 15, 20, 15]
        for i, width in enumerate(column_widths):
            worksheet.set_column(i, i, width)
        
        # Format header
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#D3D3D3'})
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        # Format cells
        cell_format = workbook.add_format({'align': 'center'})
        for row_num in range(1, len(df) + 1):
            for col_num in range(len(df.columns)):
                worksheet.write(row_num, col_num, df.iloc[row_num - 1, col_num], cell_format)

# Main function
def main():
    teams = get_team_data()
    point_table = create_point_table(teams)
    print("\nPoint Table:")
    print(point_table)
    
    # Export to Excel file
    export_to_excel(point_table, 'point_table.xlsx')

if __name__ == "__main__":
    main()
















