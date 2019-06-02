public class Solution
{
    public string NextClosestTime(string time)
    {
        if (string.IsNullOrWhiteSpace(time)) return "";

        var minutes = TimeInMinutes(time);
        var set = new HashSet<string>(time.ToCharArray());

        while (true)
        {
            minutes = (minutes + 1) % (24 * 60);
            var current = TimeString(minutes);
            if (IsValid(set, current)) return current;
        }       
    }

    private int TimeInMinutes(string time)
    {
        var split = time.Split(':');
        var hh = int.Parse(split[0]);
        var mm = int.Parse(split[1]);
        return 60 * hh + mm;
    }

    private string TimeString(int minutes)
    {
        var mm = minutes % 60;
        var hh = minutes / 60;
       return hh.ToString("00") + ":" + mm.ToString("00");
    }

    private bool IsValid(HashSet<string> set, string time2)
    {
        foreach (char c in time2)
        {
            if (!set.Contains(c)) return false;
        }
        return true;
    }
}