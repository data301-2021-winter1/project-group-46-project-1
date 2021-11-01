{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec36f1af-1b2a-4317-9d81-8fa228943fc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pylab as plt\n",
    "import seaborn as sns    #Understanding my variables\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bde7e762-3903-423a-8611-0ba019513a88",
   "metadata": {},
   "outputs": [],
   "source": [
    "path0 = \"../data/raw/Player_Attributes.csv\"\n",
    "pko = pd.read_csv(path0)\n",
    "\n",
    "def first_python_module(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data,rename columns, get rid of null values and drop necessary data with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "           .drop(['NBA_FLAG','JERSEY','PIE','TEAM_ABBREVIATION','TEAM_ID','ALL_STAR_APPEARANCES','GAMES_PLAYED_CURRENT_SEASON_FLAG','FROM_YEAR','TO_YEAR','DLEAGUE_FLAG','TEAM_CODE','TEAM_CITY','DISPLAY_FIRST_LAST','PLAYER_SLUG','FIRST_NAME','LAST_NAME','DISPLAY_FI_LAST','GAMES_PLAYED_FLAG','PLAYERCODE'], axis=1)\n",
    "\t       .rename(columns={'DISPLAY_LAST_COMMA_FIRST': 'FULL NAME', 'PTS':'PPG', 'AST':'APG','REB':'RBG'})\n",
    "           .dropna(axis=0)\n",
    "      )\n",
    "    \n",
    "    return df1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "734e10b8-7b75-4b2c-bf89-f80aa7bd926b",
   "metadata": {},
   "source": [
    "## I want to find out the tallest best player and shortest best player\n",
    "   I used just one dataset because it had most of the information I was looking for and was appropriate enough.\n",
    "   I removed columns that I found to be redundant and useless and also renamed some so I would have a better   understanding of it. I experimented with just a few data visualizations which I still think I should do more of so I can accurately answer my question to a tee. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
