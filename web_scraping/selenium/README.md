# Cookie Clicker Bot Project

## Overview

This advanced Python project leverages Selenium to automate gameplay in the popular browser game **Cookie Clicker**. The bot uses a sophisticated decision-making algorithm to optimize cookie production by continuously clicking the cookie and strategically purchasing upgrades and buildings. The goal is to maximize efficiency and Cookies Per Second (CPS) through dynamic ROI evaluation.

## Features

- **Automated Cookie Clicking**: The bot continuously clicks the cookie to generate cookies.
- **Dynamic ROI Evaluation**: Uses an intelligent algorithm to calculate the Return on Investment (ROI) for buildings and upgrades.
- **CPS Analysis**: Simulates hover actions to extract CPS information for each building dynamically.
- **Strategic Purchases**: Prioritizes high-ROI purchases to maximize long-term gains while balancing small, necessary investments.
- **Failsafe Mechanism**: Implements a limit for small, low-ROI purchases to prevent inefficiency.

## Algorithm Breakdown

### Key Functions

1. **`text_to_number(text)`**  
   Converts text-based numbers (e.g., "2.3 million") into numeric values for calculations.  
   - Supports large scales like million, billion, etc.
   - Handles commas and invalid inputs gracefully.

2. **`get_CPS(product_num)`**  
   - Simulates hover actions using Selenium's `ActionChains` to retrieve the CPS of a building or upgrade.
   - Uses explicit waits to ensure the data is loaded before accessing it.

3. **`ROI(CPS, price)`**  
   - Computes the efficiency of a building or upgrade based on its CPS and price:
     \[
     ROI = \frac{CPS}{\text{price}}
     \]
   - Higher ROI values indicate better investments.

4. **`best_to_buy(current_cookies)`**  
   - Dynamically evaluates all buildings and upgrades.
   - Filters out options based on affordability and strategic thresholds:
     - High-ROI purchases within 30%-200% of the current cookies are prioritized.
     - Small purchases (below 30% of current cookies) are allowed up to a defined limit.
   - Sorts all options by ROI and selects the best one.

### Decision-Making Logic

- **Real-Time Data Collection**:  
   Gathers live data from the game, including current cookie count, CPS of each building, and their prices.

- **Dynamic Budgeting**:  
   Considers current cookies and sets thresholds for small and large investments.  
   Example: Avoids overspending on low-impact purchases but still utilizes idle resources efficiently.

- **Failsafe Behavior**:  
   Ensures the bot continues functioning even if some elements (e.g., CPS tooltips) fail to load.

## Installation

1. Install Python 3.9 or higher.
2. Install required libraries:
   pip install selenium

