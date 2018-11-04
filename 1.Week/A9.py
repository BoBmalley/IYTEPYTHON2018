#A9
text = """
As described previously, the captured views provide us two important data: 1) 
silhouettes of the object from different views, which define the visual hull of the object, and 
2) ray-ray correspondences before and after rays intersecting with the object, which correlate to light 
refraction paths and surface geometry details.
"""
text=text.replace(',',' ')
text=text.replace(':',' ')
text=text.replace('1',' ')
text=text.replace('2',' ')
text=text.replace(')',' ')
text=text.replace('.',' ')
text=text.replace('  ',' ')
print(text)
