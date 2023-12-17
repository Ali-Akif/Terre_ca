# -*- coding: utf-8 -*-


# Créez un programme qui affiche son nom de fichier

file_path = __file__
file_segmentation = file_path.split("\\")
file_name = file_segmentation[-1]

print(file_name) 