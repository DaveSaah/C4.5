def fit_naive_bayes(attributes, target):
    target_probs = {}
    attributes_probs = {}

    # Calculate target probabilities
    unique_target_counts = target.value_counts()    #O(n) time complexity of the value counts function
    total_samples = len(target)
    for target_label, count in unique_target_counts.items():
        target_probs[target_label] = count / total_samples

    # Calculate feature probabilities
    for feature in attributes.columns:
        attributes_probs[feature] = {}
        for target_label in target_probs:
            target_subset = attributes[target == target_label][feature]
            feature_value_counts = target_subset.value_counts()
            total_class_samples = len(target_subset)
            attributes_probs[feature][target_label] = {}
            for value, count in feature_value_counts.items():
                attributes_probs[feature][target_label][value] = count / total_class_samples