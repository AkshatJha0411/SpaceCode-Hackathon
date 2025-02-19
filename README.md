### Update : We clutched the podium by bagging the 3rd spot 🎉

# Introduction

This project was developed as part of **SpaceCode Challenge 2025**, a two-day hackathon hosted by the **Space Technology and Astronomy Cell (STAC)**, IIT Mandi. The competition challenged participants to solve computational and theoretical problems in the domain of astrophysics, including exoplanet analysis, orbital mechanics, and pulsar classification. 

Our team, **Blue Explorers**, consisting of [Harsh Vardhan Sharma](https://github.com/code-master-harsh/), [Akshat Jha](https://github.com/AkshatJha0411/), and [Bhavya Sunkari](https://github.com/Bhavya445), collaborated to tackle these problems with innovative approaches and efficient coding techniques. Through this journey, we explored the realms of computational astronomy, developed new insights, and applied advanced algorithms to complex astronomical datasets.

We hope you enjoy diving into our solutions as much as we enjoyed building them!

# **Problem 01: Analysis of Exoplanets Based on Orbital Time Period** 
### **Approach to Dataset and Histogram Generation** 
1. **Data Collection**: 
   1. Accessed the exoplanet catalog via the provided link. 
   1. Filtered data to include only confirmed exoplanets detected using the Radial Velocity (RV) method. 
   1. Exported relevant parameters, particularly the orbital period (in Earth days). 
1. **Data Cleaning**: 
   1. Removed entries with missing or erroneous orbital period data. 
   1. Limited the orbital period range to 0–400 Earth days to focus on short to moderately long-period planets, avoiding skewness from extreme outliers. 
1. **Histogram Generation**: 
- Used Python’s matplotlib and seaborn libraries for visualization. 
- Binned data into intervals of 10 days, plotted the histogram, and added labels for clarity. 
#### **Key Insights** 
1. **Concentration of Short-Period Exoplanets**: 
- Most exoplanets detected via the RV method exhibit orbital periods less than 50 days. This is due to: 
- **Observational Bias**: Closer planets cause larger and more frequent Doppler shifts, making them easier to detect. 
- **Detection Sensitivity**: Short-period planets induce stronger gravitational tugs, producing higher velocity amplitudes. 
2. **Scarcity of Long-Period Exoplanets**: 
- Longer orbital periods result in weaker Doppler shifts and require more extended observation times to detect multiple cycles. 
- Current technology limits and observational time constraints hinder the detection of Earth-like planets with orbital periods similar to Earth, Venus, or Mars.
# **Problem 02: Radial Velocity Method for Finding Exoplanets** 
### **Analysis of 51 Pegasi Radial Velocity Data** 
1. **Scatter Plot**: 
   1. Loaded the radial velocity dataset. 
   1. Plotted time (Julian date) on the X-axis and radial velocity (m/s) on the Y-axis. 
   1. Observed periodic oscillations indicative of the planet’s influence. 
1. **Initial Period Estimate**: 
   1. Identified a repeating pattern visually, estimating an orbital period of approximately 4.2 days. 
1. **Lomb-Scargle Periodogram**: 
   1. Applied the periodogram formula to identify the period with the highest power. 
   1. Estimated a precise orbital period of ~4.23 days. 
1. **Phase Folding**: 
   1. Folded the radial velocity data using the derived orbital period. 
   1. Plotted the phase-folded radial velocity curve to reveal the periodic motion of the star. 
#### **Key Observations:** 
- The derived orbital period matches historical observations of 51 Pegasi b. 
- Noise in the folded curve may be due to measurement uncertainties or additional system factors.
# **Problem 03: Pulsars in Deep Space** 
## Numerical Dataset Analysis
### Data Preprocessing: 
- Scaled numerical features using StandardScaler from scikit-learn.
- Split data into training and validation sets (80:20 ratio). 
### Model Development: 
- Trained a Random Forest model with hyperparameter tuning (e.g., tree depth and the number of estimators). 
### Performance Evaluation: 
- Metrics used: Accuracy, precision, recall, F1 score, and ROC-AUC. 
- Achieved high precision, reducing false positives. 
- Performance Summary: 
  - Accuracy: 93.25% 
  - Precision: 88.97% 
  - Recall: 91.54% 
  - F1 Score: 90.23% 
  - ROC-AUC: 96.78% 
### Advantages and Limitations: 
- Advantages: 
  - Faster training and easier preprocessing. 
  - High interpretability using metrics like feature importance. 
- Limitations: 
  - Limited to structured data. 
  - Performance depends on feature engineering.
## Image Dataset Analysis 
### Image Preprocessing: 
- Resized images to 64x64 pixels. 
- Normalized pixel values and created batches for training. 
### CNN Model: 
- Designed a 4-layer CNN with convolutional, pooling, and fully connected layers. 
- Used cross-entropy loss and Adam optimizer. 
- Applied mixed precision training (GradScaler) and GPU acceleration.** 
### Performance Evaluation: 
- Validation Accuracy: 87.5%. 
- Training Loss: Converged to ~0.02 after 10 epochs. 
### Advantages and Limitations: 
- Advantages: 
  - Able to capture complex spatial patterns in images. 
  - Does not require manual feature engineering; instead, it learns features automatically. 
- Limitations: 
  - Requires significant computational resources (e.g., GPUs). 
  - Slower training process due to model complexity. 
## Comparison and Discussion 
### Numerical Models (Random Forest): 
- Faster training and interpretation. 
- Suitable for structured datasets with defined features. 
- Ideal when computational efficiency and interpretability are critical. 
### Image Models (CNN): 
- Better for complex, high-dimensional image data. 
- Requires more computational resources but excels in tasks requiring intricate pattern recognition. 
#### In summary, the Random Forest model achieved higher accuracy (93.25% vs. 87.5%) and efficiency, making it preferable for structured data. However, the CNN model excelled in recognizing complex image patterns, highlighting its strength for unstructured data tasks like image classification. 
# **Problem 04: Orbital Resonances** 
### Approach to Solve the Problem

1. **Inner Planet's Orbital Period**: Applied Kepler's Third Law to calculate the orbital period of the inner planet using the semi-major axis (a = 0.8 AU). This gave an approximate orbital period of **0.716 years**.

2. **Outer Planet's Parameters**: Using the given 3:2 orbital resonance ratio, derived the orbital period of the outer planet as **1.074 years**. Substituted this into Kepler's Third Law to find the semi-major axis, approximately **1.045 AU**.

3. **Discussion**:
   - Explored the impacts of resonance on **tidal heating**, **orbital stability**, and **habitability**.
   - Highlighted potential effects like geological activity, magnetic interactions, and their implications for life.

This structured approach provided insights into both orbital mechanics and the broader implications of resonance.
# **Problem 05: Escape Velocity from a White Dwarf** 
### Approach to Solve the Problem

1. **Escape Velocity Formula**: Derived the formula for escape velocity using conservation of energy. The final expression is:  

<div align="center">

$$v_{\text{escape}} = \sqrt{\frac{2GM}{r}}$$

</div>

2. **Numerical Calculation**: Substituted values for a white dwarf's mass (`M = 1.4 M⊙`) and radius (`r = 0.008 R⊙`) into the formula. Calculated `v_escape` as approximately `8.17 × 10^6` m/s, which is about **2.7% of the speed of light**.

3. **Discussion**:
   - Explored the role of **electron degeneracy pressure** in supporting the white dwarf against gravitational collapse.
   - Analysed the formation of **accretion disks** and their bright emissions due to the high escape velocity.
   - Highlighted how a white dwarf nearing the **Chandrasekhar limit** could trigger a Type Ia supernova.

This methodical approach connects the mathematical derivation to its astrophysical implications.
