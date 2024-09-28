
from DuplicateRemover import DuplicateRemover

dirname = 'C:\\GIT\\Duplicate-Remover\\test-images'
# dirname = 'E:\\AlexAndEmilyPhotoLibrary\\Consolidated\\PhotoLibrary'

# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
# dr.find_similar("IMG-20110704-00007.jpg",70)

