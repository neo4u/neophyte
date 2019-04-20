def str_list(head)
    str = ""

    while head.next
        str += "#{head.val}->"
        head = head.next
    end
    str += "#{head.val}"

    str
end