# NBA Shot Outcome Predictor Data Repository

This repository contains datasets used for the NBA Shot Outcome Predictor project.

## Contents

- **nba_seasons_1980_to_2024.csv** – A list of NBA seasons from 1980–81 through 2024‑25.  This file can be used to loop over seasons when pulling additional data.
- **team_data.csv** – Compiled team-level statistics (basic and advanced metrics) for each team from the 1980–81 through 2019 seasons.
- **nba_2024_shots dataset** – Shot log data for the 2024‑25 regular season.  Because GitHub has a 25 MB upload limit, the file has been split into multiple segments:
  - `nba_2024_shots_part_ac` (approx. 5 MB)
  - `aa_part_00`, `aa_part_01`, `aa_part_02`, `aa_part_03` – first 20 MB segment broken into 4 pieces of ~5 MB each
  - `ab_part_00`, `ab_part_01`, `ab_part_02`, `ab_part_03` – second 20 MB segment broken into 4 pieces of ~5 MB each

## Reconstructing the 2024 shots file

To rebuild the full `nba_2024_shots.csv` on your local machine, concatenate the pieces in order.  For example on Linux or macOS:

```bash
# combine the aa_part_* pieces back into the first segment
cat aa_part_00 aa_part_01 aa_part_02 aa_part_03 > nba_2024_shots_part_aa.csv

# combine the ab_part_* pieces back into the second segment
cat ab_part_00 ab_part_01 ab_part_02 ab_part_03 > nba_2024_shots_part_ab.csv

# finally combine all segments into the full file
cat nba_2024_shots_part_aa.csv nba_2024_shots_part_ab.csv nba_2024_shots_part_ac > nba_2024_shots.csv
```

These files were sourced from publicly available NBA datasets and are provided here for model training and analysis.  The large shot log has been split to comply with GitHub's upload limits.

Feel free to clone or fork this repository and use the data for your own analytics projects.
