class MyCalendar
  def initialize()
    @calendar = []
  end

  def book(s1, e1)
    @calendar.each do |s2, e2|
      return false if s2 < e1 && s1 < e2
    end

    @calendar.push([s1, e1])
    true
  end
end