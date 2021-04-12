setImageType('FLUORESCENCE');
classifyDetectionsByCentroid("droplets")
resetSelection();
createDetectionsFromPixelClassifier("droplets", 1000.0, 0.0, "SPLIT")
selectAnnotations();
addPixelClassifierMeasurements("droplets", "droplets")
saveDetectionMeasurements('/C:/Users/Your_Directory')
