# import requests
#
#
# def get_comments(product_id, page=1, mode=None):
#     # Define the base URL
#     url = f"https://www.digistyle.com/ajax/product/comments/list/{product_id}/"
#
#     # Prepare the parameters
#     params = {"page": page}
#     if mode:
#         params["mode"] = mode
#
#     # Send the GET request
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()  # Raise an error for bad responses
#
#         # Process the response
#         if page > 1:
#             # Append response to existing comments (you would handle this in your UI)
#             print("Appending comments...")
#             print(response.text)  # Replace with actual appending logic
#             print(response.json())  # Replace with actual loading logic
#             print("[[[[[[[[[[[[[[[[[[response.json()]]]]]]]]]]]]]]]]]]")  # Replace with actual loading logic        else:
#             # Load new comments (you would handle this in your UI)
#             print("Loading comments...")
#             print(response.text)  # Replace with actual loading logic
#             print(response.json())  # Replace with actual loading logic
#             print("[[[[[[[[[[[[[[[[[[response.json()]]]]]]]]]]]]]]]]]]")  # Replace with actual loading logic
#
#         # Check the number of comments
#         current_comments_count = len(response.json())  # Assuming response is JSON
#         if current_comments_count >= 15:
#             print("More comments available.")
#             # Logic to show "more comments" button
#         else:
#             print("No more comments available.")
#
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#
#
# # Example usage
# product_id = 191146  # Replace with the actual product ID
# get_comments(product_id, page=3, mode="json")
# import pandas as pd
#
# # خواندن فایل CSV و قرار دادن داده‌ها در ستون‌های مختلف
# df = pd.read_csv("comments.csv")
#
# # نمایش داده‌ها
# print(df.head())
#
# df.to_csv("output.csv", index=False)
