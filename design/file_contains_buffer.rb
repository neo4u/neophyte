# Given the below file API, implment file_contains(filename, buffer) to check if file contains a buffer
# def file_contains(filepath, buffer):
     # type: (typing.Text, bytes) -> bool
# end
# def file_open(filepath):
    # return file
# end

# def file_read(file, bytes, start_byte=0):
    # something
    # return str .  # bytes long
# end

# Constraints
# 1. File is really large in TBs
# 2. Buffer is very small relative to the file (100s of MBs)

# O(n * (b_size ^ 2))
def file_contains(filepath, buffer)
    f_size = sizeof(filepath)
    b_size = buffer.size
    return false if f_size < b_size

    file = file_open(filepath)
    magic_bytes = buffer[0, 2]
    rem_b_size = b_size # remaining bytes to be matched
    b_offset, f_offset = 0, 0
    f_bytes = nil
    partial_match = false

    while f_bytes != 0
        f_bytes = file_read(file, b_size, f_offset)
        f_offset += f_bytes
        magic_bytes = buffer[b_offset, 2] if partial_match

        if !check_chunk_for_header(f_bytes, magic_bytes)
            partial_match = false
            rem_b_size, b_offset, magic_bytes = b_size, 0, buffer[0, 2]
            next
        end

        match_size = check_chunk_for_buffer(f_bytes, buffer, b_offset)
        if match_size > 0 && !partial_match
            partial_match = true
            rem_b_size -= match_size
            b_offset += match_size
        elsif match_size == 0 && partial_match
            rem_b_size, b_offset, magic_bytes = b_size, 0, buffer[0, 2]
        end

        return true if 0 == rem_b_size
    end

    false
end

# O(b_size)
def check_chunk_for_header(chunk, magic_bytes)
    0.upto(chunk.size - 1) do |i|
        return true if chunk[i, 2] == magic_bytes
    end

    false
end

# O(b_size ^ 2)
def check_chunk_for_buffer(chunk, buffer, b_offset)
    b_size = buffer.size
    found = true
    match_size = 0, 0

    0.upto(b_size - 1) do |i|
        match_size, found = 0, true
        b_offset.upto(b_size - 1 - b_offset - i) do |j|
            if chunk[i + j] != buffer[j] # TODO: fix
                found = false
                break
            else
                match_size += 1
            end
        end
    end

    !found ? 0 : match_size
end


# Follow-up questions
# 1. How will you optimize the number of file reads?
# A. Read multiples of b_size at a time. Ex: 4 * b_size reduce the reads by 4 times

# 2. Can we reduce the speed by using message digests?
# A: - We can replace the method check_chunk_for_buffer with the method below
#      which reduces the complexity to O(b_size) from O(b_size)
#    - We can also use message digests to eliminate all chunks that have the same hash
#      as eliminated chunks

# Time to take a digest (questionable??) + O(digest_size) (digest size is constant)
def check_chunk_with_digest(chunk, buffer, b_offset)
    b_size = buffer.size
    found = true
    match_size = 0

    0.upto(b_size - 1) do |i|
        if digest(chunk[i...b_size].to_s) != digest(buffer[b_offset...b_size].to_s)
            next
        else
            match_size = b_size - 1 - i
        end
    end

    !found ? 0 : match_size
end
