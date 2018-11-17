def odd_even_list(head)
    return head if head.nil? || head.next.nil?
    even_head, even_tail, odd_tail, runner = head.next, head.next, head, head.next.next
    count = 1

    # Runner starts from third node but count start from 1 which so the odd/even offset remains
    while runner
        if count.even?
            even_tail.next, even_tail = runner, runner
        else
            odd_tail.next, odd_tail = runner, runner
        end
        runner = runner.next
        count += 1
    end

    odd_tail.next = even_head
    even_tail.next = nil

    head
end
