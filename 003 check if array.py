def is_int_array(a):
      return isinstance(a, list) and  all(isinstance(x, (int, float)) and x == int(x) for x in a)



print(is_int_array([1, "codew", 3, 4]))#, False, "Input: [1, 2, 3, 4]")
print(is_int_array([-11, -12, -13, -14]))#, True, "Input: [-11, -12, -13, -14]")
print(is_int_array([1.0, 2.0, 3.0]))#, True, "Input: [1.0, 2.0, 3.0]")
print(is_int_array([1, 2, None]))#, False, "Input: [1,2, None]")
print(is_int_array([])) #true
print(is_int_array(None)) #false
print(is_int_array([1,2, None])) # : false should equal False
print(is_int_array([1.0, 2.0, 3.0001])) #: false should equal False
print(is_int_array(['-1'])) #: True should equal False