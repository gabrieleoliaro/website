import os,sys,argparse,errno

def valid_file_path_arg_type(filepath):
    if os.path.isfile(filepath):
        return filepath
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filepath)

def valid_directory_path_arg_type(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--stub_file', type=valid_file_path_arg_type, required=True, help="path to the file containing the stub of the html portfolio snippet")
	parser.add_argument('-l', '--links_folder', type=valid_directory_path_arg_type, required=True, help="path to the folder containing the files with the links")
	parser.add_argument('-o', '--output_file', required=True, help="path to the output file")

	args = parser.parse_args()

	linksfolder = args.links_folder
	outputfile = open(args.output_file, 'w')

	patterns = ("filter-milan", "milan_link1.jpg", "Milan 1", "Milan")
	replacements = ()

	for links_filename in os.listdir(linksfolder):

		linksfile = open(os.path.join(linksfolder, links_filename), 'r')

		line_n = 0
		place_str = ""
		place_str_simplified = ""

		for line in linksfile:
			if line_n == 0:
				place_str = str(line).replace("\n","")
				place_str_simplified = place_str.lower().replace(" ", "")
				line_n += 1
				continue
			
			replacements =("filter-{}".format(place_str_simplified), str(line).replace("\n",""), "{} {}".format(place_str, line_n), "{}".format(place_str))
			stubfile = open(args.stub_file, 'r')
			for line2 in stubfile:
				for pattern, replacement in zip(patterns, replacements):
					line2 = line2.replace(pattern, replacement)
				outputfile.write(line2)
			stubfile.close()
			outputfile.write("\n\n")
			
			line_n += 1

		linksfile.close()
	outputfile.close()