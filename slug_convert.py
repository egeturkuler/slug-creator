import re

def string_to_slug(input_string):
    # Remove special characters and replace spaces with hyphens
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', input_string)
    slug = slug.lower().strip().replace(' ', '-')
    
    # Remove consecutive hyphens
    slug = re.sub(r'[-]+', '-', slug)
    
    return slug

# Example usage:
input_string = "This is a String with Special Characters! @#$ Ep 31 season 69"
slug = string_to_slug(input_string)
print(slug)  # Output: "this-is-a-string-with-special-characters"