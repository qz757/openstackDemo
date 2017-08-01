rm -rf AUTHORS 
rm -rf dist
rm -rf ChangeLog 
rm -rf openstackDemo.egg-info/
rm -rf build
rm -rf .eggs
find . -name "*.pyc" -type f -print -exec rm -rf {} \; 
