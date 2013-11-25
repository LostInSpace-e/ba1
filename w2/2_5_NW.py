import sys

masses={'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114, 'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
rev_masses={57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C', 113:'I', 114:'N', 115:'D', 128:'K', 129:'E', 131:'M', 137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'}

def main():
	experimental_spectra =[0,87,87,87,87,99,99,113,114,128,128,128,128,128,129,147,147,147,156,186,186,201,215,215,215,216,227,227,234,242,242,243,246,256,273,275,275,285,299,303,314,314,329,329,330,333,343,362,370,371,372,374,374,390,390,403,413,420,428,442,442,443,446,457,458,461,461,477,500,500,502,502,515,517,518,518,519,541,548,571,574,575,576,586,587,589,589,604,605,616,628,629,630,647,661,662,663,665,675,688,699,703,703,704,715,717,717,727,733,734,744,752,757,762,776,790,790,791,803,814,816,817,831,831,832,845,846,851,862,874,877,885,890,890,890,904,904,918,938,938,944,945,946,959,960,961,961,964,977,991,1002,1018,1018,1032,1032,1032,1033,1037,1046,1047,1051,1058,1073,1089,1105,1105,1108,1117,1119,1124,1130,1131,1145,1147,1160,1160,1165,1175,1179,1180,1180,1204,1217,1223,1233,1236,1237,1244,1247,1252,1259,1264,1267,1274,1275,1278,1288,1294,1307,1331,1331,1332,1336,1346,1351,1351,1364,1366,1380,1381,1387,1392,1394,1403,1406,1406,1418,1422,1438,1453,1460,1464,1465,1474,1478,1479,1479,1479,1493,1493,1509,1520,1534,1547,1550,1550,1551,1552,1565,1566,1567,1573,1573,1593,1607,1607,1621,1621,1621,1626,1634,1637,1649,1660,1665,1666,1679,1680,1680,1694,1695,1697,1708,1720,1721,1721,1735,1749,1754,1759,1767,1777,1778,1784,1794,1794,1796,1807,1808,1808,1812,1823,1836,1846,1848,1849,1850,1864,1881,1882,1883,1895,1906,1907,1922,1922,1924,1925,1935,1936,1937,1940,1963,1970,1992,1993,1993,1994,1996,2009,2009,2011,2011,2034,2050,2050,2053,2054,2065,2068,2069,2069,2083,2091,2098,2108,2121,2121,2137,2137,2139,2140,2141,2149,2168,2178,2181,2182,2182,2197,2197,2208,2212,2226,2236,2236,2238,2255,2265,2268,2269,2269,2277,2284,2284,2295,2296,2296,2296,2310,2325,2325,2355,2364,2364,2364,2382,2383,2383,2383,2383,2383,2397,2398,2412,2412,2424,2424,2424,2424,2511]
						# FIEA [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460]
	N = 455
	#experimental_spectra =[0,71,71,87,97,99,99,101,101,101,113,113,114,114,115,115,115,115,128,128,128,129,131,137,172,186,186,196,199,200,212,215,216,216,218,227,227,227,228,229,229,230,234,242,246,252,257,287,287,287,297,314,316,317,326,328,328,331,333,333,340,341,341,343,344,346,349,355,356,367,388,402,402,404,415,415,425,427,434,439,443,445,447,448,454,455,456,458,461,464,468,469,469,503,512,516,517,529,532,532,539,540,542,546,549,553,562,562,563,565,568,570,571,574,582,583,618,630,631,633,636,642,643,649,654,654,655,660,661,661,664,664,673,677,681,682,683,685,696,732,735,743,745,746,751,755,756,758,760,761,764,765,767,769,780,782,786,789,792,798,810,810,829,836,850,852,857,858,860,860,869,873,879,881,882,883,888,890,893,895,895,897,900,911,938,951,951,964,966,968,970,972,973,980,980,987,989,989,996,997,1001,1009,1010,1010,1013,1026,1039,1051,1052,1069,1079,1079,1081,1085,1086,1087,1088,1094,1094,1097,1100,1102,1110,1110,1111,1115,1124,1125,1127,1154,1166,1180,1180,1182,1184,1185,1193,1196,1198,1200,1201,1207,1209,1214,1216,1223,1224,1225,1225,1225,1226,1228,1255,1267,1294,1296,1297,1297,1297,1298,1299,1306,1308,1313,1315,1321,1322,1324,1326,1329,1337,1338,1340,1342,1342,1356,1368,1395,1397,1398,1407,1411,1412,1412,1420,1422,1425,1428,1428,1434,1435,1436,1437,1441,1443,1443,1453,1470,1471,1483,1496,1509,1512,1512,1513,1521,1525,1526,1533,1533,1535,1542,1542,1549,1550,1552,1554,1556,1558,1565,1571,1571,1584,1611,1622,1625,1627,1627,1629,1632,1634,1639,1640,1641,1643,1649,1653,1662,1662,1664,1665,1670,1672,1686,1693,1712,1712,1724,1730,1733,1736,1740,1742,1753,1755,1757,1758,1761,1762,1764,1766,1767,1771,1776,1777,1779,1787,1790,1826,1837,1839,1840,1841,1845,1849,1858,1858,1861,1861,1862,1867,1868,1868,1873,1879,1880,1886,1889,1891,1892,1904,1939,1940,1948,1951,1952,1954,1957,1959,1960,1960,1969,1973,1976,1980,1982,1983,1990,1990,1993,2005,2006,2010,2019,2053,2053,2054,2058,2061,2064,2066,2067,2068,2074,2075,2077,2079,2083,2088,2095,2097,2107,2107,2118,2120,2120,2134,2155,2166,2167,2173,2176,2178,2179,2181,2181,2182,2189,2189,2191,2194,2194,2196,2205,2206,2208,2225,2235,2235,2235,2265,2270,2276,2280,2288,2292,2293,2293,2294,2295,2295,2295,2304,2306,2306,2307,2310,2322,2323,2326,2336,2336,2350,2385,2391,2393,2394,2394,2394,2407,2407,2407,2407,2408,2408,2409,2409,2421,2421,2421,2423,2423,2425,2435,2451,2451,2522]
	#N = 438
	single_peptides = set()
	# step 1 : Populate 0 peptide
	populate_0_peptide(single_peptides, experimental_spectra)
	# step 2 : Initializet the master peptide list
	leaderboard  = set(single_peptides)
	leader_peptide = list(single_peptides)[0]
	leader_peptide_score = score(leader_peptide, experimental_spectra)

	parent_mass_spectrum = get_parent_mass(experimental_spectra)
	print 'Parent Mass Spectrum ==>',parent_mass_spectrum
	print generate_theoretical_spectra('FIEA', True)
	print generate_theoretical_spectra('FAEI', True)

	#step 3 : Repeat until the leaderboard it empty
	while(len(leaderboard) != 0):
		#step 4 : add the single peptides in various positions of the elements of the master list
		leaderboard = expand(single_peptides, leaderboard)
		temp_leaderboard = set()
		for peptide in leaderboard:
			#print 'PEPTIDE ==>',peptide
			peptide_mass = get_mass(peptide)
			if peptide_mass == parent_mass_spectrum:
				if score(peptide, experimental_spectra) >= leader_peptide_score:
					leader_peptide = peptide
					leader_peptide_score = score(leader_peptide, experimental_spectra)
					temp_leaderboard.add(peptide)
					print 'CURRENT LEADER ==> ', formatted_print(leader_peptide)
			elif peptide_mass < parent_mass_spectrum:
				temp_leaderboard.add(peptide)
		leaderboard = cut(temp_leaderboard, experimental_spectra, N)

	#step 7 : show formatted results
	print 'FORMATTED RESULT ==> ', formatted_print(leader_peptide)

def cut(leaderboard, experimental_spectra, N):
	candidate_score_list = []
	sorted_score_set = []
	for candidate in leaderboard:
		score_val = score(candidate, experimental_spectra)
		candidate_score_list.append([candidate, score_val])
		sorted_score_set.append(score_val)
	sorted_score_set.sort()

	set_length = len(sorted_score_set)
	print "SET_LENGTH ==>",set_length
	cutoff = sorted_score_set[set_length - N] if set_length > N else -1
	print 'CUTOFF ==>',cutoff
	temp_leaderboard = set()
	for entry in candidate_score_list:
		if entry[1] >= cutoff:
			temp_leaderboard.add(entry[0])
	return temp_leaderboard


def score(peptide, experimental_spectra):
	theoretical_spectra = generate_theoretical_spectra(peptide, True)
	temp_experimental = list(experimental_spectra)
	matches = 0
	for mass in theoretical_spectra:
		if mass in temp_experimental:
			matches += 1
			temp_experimental.remove(mass)
	return matches


def get_parent_mass(spectrum):
	index = 1
	max = spectrum[0]
	while(index < len(spectrum)):
		if spectrum[index] > max:
			max = spectrum[index]
		index += 1
	return max

def formatted_print(peptide_str):
	pep_len = peptide_str.__len__()
	index = 0
	result_list = []
	while(index < pep_len):
		result_list.append(str(masses[peptide_str[index]]))
		index += 1
	return '-'.join(result_list)

def expand(single_peptides, master_set):
	temp_list = []
	for single in single_peptides:
		for string in master_set:
			str_len = string.__len__()
			index = 0
			while(index < str_len):
				l_str = string[0:index]
				r_str = string[index:str_len]
				temp_list.append(l_str + single + r_str)
				index += 1
	return temp_list

def populate_0_peptide(peptide_list, experimental_spectra):
	for mass in experimental_spectra:
		if mass in rev_masses:
			peptide_list.add(rev_masses[mass])
	return peptide_list

# if exact match : return 1, if inconsistency : return 0, if potential match : return 0
def compare_spectra(theoretical, experimental):
	temp_experimental = list(experimental)
	for mass in theoretical:
		if mass not in temp_experimental:
			return -1
		else:
			temp_experimental.remove(mass)

	if len(experimental) == len(theoretical):
			return 1
	return 0

def generate_theoretical_spectra(source, cyclo):
	size = 1
	max_len = source.__len__()
	mass_list = [0]
	while(size <= max_len - 1):
		if cyclo:
			generate_cyclo_combinations(mass_list, source, size)
		else:
			generate_linear_combinations(mass_list, source, size)
		size += 1
	mass_list.append(get_mass(source))

	mass_list.sort()
	return mass_list


def generate_linear_combinations(mass_list, source, size):
	max_len = source.__len__()
	index = 0
	while(index <= max_len - size):
		size_index = 0
		string =''
		while(size_index < size):
			string += source[(size_index + index)]
			size_index += 1
		index += 1
		mass_list.append(get_mass(string))

def generate_cyclo_combinations(mass_list, source, size):
	max_len = source.__len__()
	index = 0
	while(index < max_len):
		size_index = 0
		string =''
		while(size_index < size):
			string += source[(size_index + index) % max_len]
			size_index += 1
		index += 1
		mass_list.append(get_mass(string))

def get_mass(string):
	sum = 0
	index = 0
	while(index < string.__len__()):
		sum += masses[string[index]]
		index += 1
	return sum

if __name__ == '__main__':
	main()