//Setup the image output
run("Colors...", "foreground=white background=black selection=red");

//Duplicate with specific name
run("Duplicate...", "title=droplets");
run("Duplicate...", "title=measure");

//Segmentation and droplets detection
selectWindow("droplets");
setAutoThreshold("Default dark");
setThreshold(1507, 65535);
run("Convert to Mask");
run("Watershed");

//Droplets measurement
run("Set Measurements...", "area standard mean centroid perimeter median display redirect=measure decimal=1");
run("Analyze Particles...", "size=22500-62500 circularity=0.00-1.00 show=Outlines display exclude add");

//
roiManager("Show None");
roiManager("Show All");
run("Flatten");
