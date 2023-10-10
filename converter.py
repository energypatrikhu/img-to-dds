import os
import sys
from wand import image

try:
    base_input_dir_path = "./input"
    base_output_dir_path = "./output"

    img_sizes = [32, 64, 128, 256]

    if not os.path.exists(base_input_dir_path):
        print("Error: 'input' folder does not exists!")
        print("")
        input("Press [Enter] to continue.")
        sys.exit(1)

    if not os.path.exists(base_output_dir_path):
        os.mkdir(base_output_dir_path)

    input_dir_list = os.listdir(base_input_dir_path)

    for filename in input_dir_list:
        for size in img_sizes:
            with image.Image(filename=f"{base_input_dir_path}/{filename}") as img:

                output_filename_wo_ext = os.path.splitext(filename)[0]

                print(
                    f"Converting '{base_input_dir_path}/{filename}' to '{base_output_dir_path}/{output_filename_wo_ext}_{size}.dds'"
                )

                img.compression = "dxt5"
                img.transform(resize=f"{size}x{size}")
                img.save(
                    filename=f"{base_output_dir_path}/{output_filename_wo_ext}_{size}.dds"
                )
        print("")

    print("Done!")
    print("")
    input("Press [Enter] to continue.")

except Exception as error:
    print("!!!ERROR!!!")
    print(error)
    print("!!!ERROR!!!")
    print("")
    input("Press [Enter] to continue.")
