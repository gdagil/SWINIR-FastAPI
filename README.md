
# SWINIR-FastAPI
API for [SwinIR](https://github.com/JingyunLiang/SwinIR)
## Fast way to use it with default settings
```bash
git clone https://github.com/gdagil/SWINIR-FastAPI.git
cd SWINIR-FastAPI
sudo docker compose up
```
### Usung the image (environment variables)
* SWINIR - all settings you can find in original [repo](https://github.com/JingyunLiang/SwinIR)
	* SWINIR_TASK
	* SWINIR_SCALE
	* SWINIR_NOISE
	* SWINIR_JPEG
	* SWINIR_TRAIN_PATCH_SIZE
	* SWINIR_LARGE_MODEL
	* SWINIR_MODEL
	* SWINIR_TILE
	* SWINIR_TILE_OVERLAP