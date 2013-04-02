a = []
(1...1000).each do |n|
  if n % 3 == 0 or n % 5 == 0
    a << n
  end
end
puts a.reduce(:+)
