class StringCalculator:
	def add(string_numbers):
		
		sum = 0
		negative_number = []	
		
		if string_numbers == '':	
			return 0

		if string_numbers.count(',') == 0 and string_numbers.count('\n') == 0:
			return int(string_numbers) if int(string_numbers) < 1000 else ''	

		if string_numbers.startswith('//'):
			sep_end = string_numbers.find('\n')
			sep = string_numbers[2:sep_end]
			string_numbers = string_numbers[sep_end + 1:]
			string_numbers = string_numbers.split(sep)

		if "," in  string_numbers:
			string_numbers = string_numbers.replace(',', '\n')

		if "\n" in string_numbers:
			string_numbers = string_numbers.split()

		
		for number in string_numbers:
			if int(number) < 0:
				negative_number.append(number)
			elif int(number) >= 1000:
				continue	
			else:	
				sum += int(number)
		if len(negative_number) > 0:
			return ('отрицательные числа запрещены: ' + ','.join(negative_number))							
		
		return sum	
						