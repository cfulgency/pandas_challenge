{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Note\n",
    "* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase ID</th>\n",
       "      <th>SN</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Item ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Lisim78</td>\n",
       "      <td>20</td>\n",
       "      <td>Male</td>\n",
       "      <td>108</td>\n",
       "      <td>Extraction, Quickblade Of Trembling Hands</td>\n",
       "      <td>3.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Lisovynya38</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>143</td>\n",
       "      <td>Frenzied Scimitar</td>\n",
       "      <td>1.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Ithergue48</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>92</td>\n",
       "      <td>Final Critic</td>\n",
       "      <td>4.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Chamassasya86</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>100</td>\n",
       "      <td>Blindscythe</td>\n",
       "      <td>3.27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Iskosia90</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>131</td>\n",
       "      <td>Fury</td>\n",
       "      <td>1.44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Purchase ID             SN  Age Gender  Item ID  \\\n",
       "0            0        Lisim78   20   Male      108   \n",
       "1            1    Lisovynya38   40   Male      143   \n",
       "2            2     Ithergue48   24   Male       92   \n",
       "3            3  Chamassasya86   24   Male      100   \n",
       "4            4      Iskosia90   23   Male      131   \n",
       "\n",
       "                                   Item Name  Price  \n",
       "0  Extraction, Quickblade Of Trembling Hands   3.53  \n",
       "1                          Frenzied Scimitar   1.56  \n",
       "2                               Final Critic   4.88  \n",
       "3                                Blindscythe   3.27  \n",
       "4                                       Fury   1.44  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import pandas as pd\n",
    "\n",
    "# File to Load (Remember to Change These)\n",
    "file_to_load = \"Resources/purchase_data.csv\"\n",
    "\n",
    "# Read Purchasing File and store into Pandas data frame\n",
    "purchase_data = pd.read_csv(file_to_load)\n",
    "purchase_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Player Count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Display the total number of players\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Players</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>576</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Total Players\n",
       "0            576"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use List Length of Screen Names \"SN\" to Determine the Total Number of Players.\n",
    "total_players = len(purchase_data[\"SN\"].value_counts())\n",
    "\n",
    "# Create a Data Frame with the Total Players Count\n",
    "player_count = pd.DataFrame({\"Total Players\":[total_players]})\n",
    "player_count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Purchasing Analysis (Total)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain number of unique items, average price, etc.\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Gender Demographics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Percentage and Count of Male Players\n",
    "\n",
    "\n",
    "* Percentage and Count of Female Players\n",
    "\n",
    "\n",
    "* Percentage and Count of Other / Non-Disclosed\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Purchasing Analysis (Gender)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Age Demographics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Establish bins for ages\n",
    "\n",
    "\n",
    "* Categorize the existing players using the age bins. Hint: use pd.cut()\n",
    "\n",
    "\n",
    "* Calculate the numbers and percentages by age group\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: round the percentage column to two decimal points\n",
    "\n",
    "\n",
    "* Display Age Demographics Table\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Purchasing Analysis (Age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Bin the purchase_data data frame by age\n",
    "\n",
    "\n",
    "* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Top Spenders"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain the results in the table below\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Sort the total purchase value column in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the summary data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Most Popular Items"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Retrieve the Item ID, Item Name, and Item Price columns\n",
    "\n",
    "\n",
    "* Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Sort the purchase count column in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the summary data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Most Profitable Items"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Sort the above table by total purchase value in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernel_info": {
   "name": "python3"
  },
  "kernelspec": {
   "display_name": "Python (PythonData)",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.6.12"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autoclose": false,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  },
  "nteract": {
   "version": "0.2.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
