import torch

def Predict(transformed_img , model, device , class_names , threshold=0.5):
    """ This function predicts the output of the image"""
    
    # Model prediction
    model.eval()  # ensure eval mode
    with torch.no_grad():  # no gradients needed for inference
        logits = model(transformed_img)
        print(f"Logits shape: {logits.shape}")  # should be (1, num_classes)
        
        # Safety check: number of output classes should match class_names length
        assert logits.shape[1] == len(class_names), \
            f"Model output ({logits.shape[1]}) != class_names length ({len(class_names)})"
        
        # Convert to probabilities
        probs = torch.softmax(logits, dim=1)
        
        # Get max probability and class index
        max_prob, pred_idx = torch.max(probs, dim=1)
        max_prob = max_prob.item()
        pred_idx = pred_idx.item()
        

    # Threshold check
    if max_prob >= threshold:
        predicted_class = class_names[pred_idx]
        
    else:
        predicted_class = "Unknown"
        
    
    class_probabilities = {
    class_names[i]: f"{prob.item() * 100:.2f}%"
    for i, prob in enumerate(probs[0])
               }


    
    
    return predicted_class, max_prob , class_probabilities