# image-dataset-augmentatator
Image augmentation pipepline for conditional GANs base on Augmentator library

## Available parameters
`--input_dir` path to directory containing the images
`--output_dir` path to directory to save new images
`--output_format` output image format (JPEG|BMP|PNG|GIF)
`--output_width` output image width in pixels
`--output_height` output image height in pixels
`--resample_filter` filter to use when resampling (BICUBIC|BILINEAR|ANTIALIAS|NEAREST)
`--sample_count` amount of new images to generate
`--zoom` zoom in randomly
`--distortion` distort randomly

## Basic execution
```bash
python3 augmentator.py
--input_dir '/home/ramiro/SoftwareProjects/datasets/databetes/gummybears_macro' 
--output_dir '/home/ramiro/SoftwareProjects/datasets/databetes/gummybears_macro/output' 
--sample_count 100 
--zoom --distortion 
```

This will do random crops and resize the images to 512px also add random zoom and distortion.
