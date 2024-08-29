## Introduction

A recommendation system is an algorithm that suggests relevant items to users by analyzing their behavior, interests, and characteristics. It interacts with users to learn their preferences, storing this information to generate new recommendations for similar users. These systems are valuable in online retail as they can increase sales by tailoring suggestions to user needs and promoting diverse items. This project will focus on two key techniques: Content-based filtering and Collaborative-based filtering (user-user and item-item).

## Objective
To optimize user satisfaction and retention by enhancing the effectiveness of anime recommendations, leveraging the growing popularity of anime.

## Datasets
- The <a href="https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database" target="_blank">datasets</a> are from the Kaggle repository that was first gathered from myanimelist.net API. 

## Project execution

- The CRISP-DM methodology was used for structured and effective project execution.

- I used descriptive statistics during EDA to understand data distribution and handle missing values.

- Content-based filtering and collaborative filtering (user-user and item-item) were used in this project.

## Results

- *Content filtering* 
  - It involves creating a user profile based on metadata (like genre, actors, directors) from explicit feedback (e.g., ratings) or implicit feedback (e.g., browsing history). This profile helps recommend similar products or services. In this project, content-based filtering was used to recommend anime based on the genre. For instance, if a user watches 'Dragon Ball,' similar anime are recommended, suggesting effective performance. However, the dataset's limited features affect the system's complexity and effectiveness.
 
- *Collaborative filtering*
  - *User-User:* I used the Pearson correlation to measure similarity between users, normalizing for different rating patterns to reduce individual biases (Aggarwal & Springer International Publishing Ag, 2018, p.34-38). Recommendations were made based on users with a similarity score of 0.8 or higher with user '72254', aiming to ensure relevant suggestions. The predicted ratings were generally moderate to low, as similar users also rated these anime lower. The model achieved a low root mean square error (RMSE) of 0.40, indicating predictions are close to actual ratings with an average deviation of 0.40 units.
 
  - *Item-Item:* In item-item collaborative filtering, the cosine function was used to determine item similarity for recommending anime to user ‘72254’. The predicted ratings are about 9, indicating strong enjoyment for the recommendations. The average RMSE of 0.74 suggests that the predictions are relatively accurate.
 
## Conclusion

The current recommender systems face challenges with new users due to limited metadata. Expanding metadata could improve recommendations and user retention, though it may add complexity. Collaborative filtering is effective for existing users but needs better content filtering for new and inactive users. A hybrid system might offer additional benefits.


#### References:
Aggarwal, C.C. and Springer International Publishing Ag (2018). Recommender Systems: The Textbook. Cham Springer International Publishing Springer.

docs.python.org. (n.d.). collections — Container datatypes — Python 3.8.3 documentation. [online] Available at: https://docs.python.org/3/library/collections.html. [Accessed 18 May 2024].

Libraries.io. (2023). missingno on Pypi. [online] Available at: https://libraries.io/pypi/missingno [Accessed 18 May 2024].

matplotlib.org. (n.d.). Getting started — Matplotlib 3.6.2 documentation. [online] Available at: https://matplotlib.org/stable/users/getting_started/index.html [Accessed 16 May 2024].

Müller, A. C. and Guido, S. (2017). Introduction to machine learning with Python: a guide for data scientists. 1st ed. United States of America. O’reilly Media.

Numpy (2009). NumPy. [online] Numpy.org. Available at: https://numpy.org/. [Accessed 16 May 2024].

OpenAI. (2024). ChatGPT (GPT-3.5 version) [Large language model]. https://chat.openai.com/chat (https://chat.openai.com/chat. [Accessed 20 May 2024])

pandas.pydata.org. (n.d.). User Guide — pandas 1.0.4 documentation. [online] Available at: https://pandas.pydata.org/docs/user_guide/index.html#user-guide. [Accessed 16 May 2024].

Patel, D., Patel, F. and Chauhan, U. (2023). Recommendation Systems: Types, Applications, and Challenges. International Journal of Computing and Digital Systems, 13(1), pp.851–868. doi:https://doi.org/10.12785/ijcds/130168.

rasbt.github.io. (n.d.). Mlxtend.frequent patterns - mlxtend. [online] Available at: https://rasbt.github.io/mlxtend/api_subpackages/mlxtend.frequent_patterns/. [Accessed 20 May 2024].

Ricci, F., Lior Rokach, Bracha Shapira and Springerlink (Online Service (2015). Recommender Systems Handbook. New York, Ny: Springer Us.

Scikit learn (2018). sklearn.feature_extraction.text.TfidfVectorizer — scikit-learn 0.20.3 documentation. [online] Scikit-learn.org. Available at: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html.[Accessed 20 May 2024].

Scikit-learn (2019). scikit-learn: machine learning in Python — scikit-learn 0.20.3 documentation. [online] Scikit-learn.org. Available at: https://scikit-learn.org/stable/index.html. [Accessed 20 May 2024].

Scipy.org. (2019). scipy.stats.pearsonr — SciPy v1.3.2 Reference Guide. [online] Available at: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html. [Accessed 21 May 2024]

Waskom, M. (2021). seaborn: statistical data visualization — seaborn 0.10.1 documentation. [online] seaborn.pydata.org. Available at: https://seaborn.pydata.org/index.html [Accessed 18 May 2024].
