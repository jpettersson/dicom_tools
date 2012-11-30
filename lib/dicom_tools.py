import dicom
import sys 

class DicomFile:
  def __init__(self, file_ref):
    self.loadFileData(file_ref)
  
  # Load the initial file data
  def loadFileData(self, file_ref):
    self.file = dicom.read_file(file_ref)

  # Overwrite the voxel data & associated tags
  # with data from another dicom file.
  def loadVoxelDataFromFile(self, file_ref):
    dcm = dicom.read_file(file_ref)

    replace = [
      'ImagePositionPatient', 
      'GridFrameOffsetVector',
      'PixelSpacing',
      'Rows',
      'Columns',
      'NumberOfFrames',
      'DoseGridScaling',
      'PixelData',
      'BitsAllocated',
      'BitsStored',
      'HighBit'
    ]

    for attr in replace:
      val = getattr(dcm, attr)
      setattr(self.file, attr, val)

  # Set a dicom tag key -> value pair.
  def set(self, name, value):
    setattr(self.file, name, value)

  # Write the current file contents to the filesystem.
  def write(self, path):
    self.file.save_as(path)