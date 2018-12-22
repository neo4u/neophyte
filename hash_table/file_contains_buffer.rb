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
    file_size = sizeof(filepath)
    b_size = buffer.size
    return false if file_size < b_size

    file = file_open(filepath)
    magic_bytes = buffer[0, 2]
    match_index, match_size = 0, 0
    rem_b_size = b_size
    b_offset = 0
    f_bytes = nil

    while f_bytes != 0
        f_bytes = file_read(file, b_size, match_index)
        next if !check_chunk_for_header(f_bytes, magic_bytes)
        match_index, match_size = check_chunk_for_buffer(f_bytes, buffer, b_offset)
        rem_b_size -= match_size
        b_offset += matched_size

        return true if 0 == rem_b_size
    end
    
    true
end

# O(b_size)
def check_chunk_for_header(chunk, magic_bytes)
    0.step(chunk.size - 1, 2) do |i|
        return true if chunk[i, 2] == magic_bytes
    end

    false
end

# O(b_size ^ 2)
def check_chunk_for_buffer(chunk, buffer)
    b_size = buffer.size
    match_idx, match_size = 0, 0
    0.upto(b_size - 1) do |i|
        0.upto(buffer.size - 1) do |j|
            if chunk[i] != buffer[j]
                return [0, 0]
            else
                match_idx += 1
                match_size += 1
            end
        end
    end

    [match_idx, match_size]
end


# Follow-up questions
# 1. How will you optimize the number of file reads?

# 2. Can we reduce the speed by using msg digests?
# A: - We can replace the method check_chunk_for_buffer with the method below which reduces the complexity to O(b_size)
#    - We can 
# O(b_size), Time to take a digest + O(digest_size)
def check_chunk_with_digest(chunk, buffer)
    b_size = buffer.size
    match_idx, match_size = 0, 0

    0.upto(b_size - 1) do |i|
        if digest(chunk[i...b_size].to_s) != digest(buffer[0...b_size - 1 - i].to_s)
            return [0, 0]
        else
            match_idx = i
            match_size = b_size - 1 - i
        end
    end

    [match_idx, match_size]
end
