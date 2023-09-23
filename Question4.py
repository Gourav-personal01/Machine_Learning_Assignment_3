# Q4. What are some drawbacks of using the Filter method for feature selection?
    
# # Answer -

# Independence of Model:
# Filter methods select features based on their statistical properties or correlations with the target 
# variable without considering the interaction between features. As a result, 
# they may not capture complex relationships that a machine learning model could exploit.

# Lack of Context:
# Filter methods do not take into account the context of the specific machine learning algorithm you plan to use. Features that are 
# deemed irrelevant by a filter method may still be useful in combination with other features within the context of a particular model.

# Loss of Information:
# In some cases, filter methods may lead to the loss of valuable information, 
# especially if features are removed without a clear understanding of their interpretability or domain relevance.