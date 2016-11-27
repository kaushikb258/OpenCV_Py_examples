python create_features.py --samples fighterPlane images/069.fighter-jet/ --samples kangaroo images/121.kangaroo-101/ --samples mars images/137.mars/ --codebook-file models/codebook.pk1 --feature-map-file models/feature_map.pk1

python training.py --feature-map-file models/feature_map.pk1 --svm-file models/svm.pk1

python classify_data.py --input-image fighterPlane.jpg --svm-file models/svm.pk1 --codebook-file models/codebook.pk1
python classify_data.py --input-image mars1.jpeg --svm-file models/svm.pk1 --codebook-file models/codebook.pk1
