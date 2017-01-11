#  * Here at RelateIQ we crawl lots of emails from our users. In order to maintain records of which emails we have already crawled we have to deal with what we call the "Email Ranges Problem".
 
# A "range" is just a pair of messages IDs, for  example  5:14 which means that we have crawled emails with ids between 5 and 14.
# Crawlers crawl several ranges at a time and then hand those ranges off to another component called the EmailRangesHistory which just a way to keep track of which emails have been crawled and which haven't.
# Problem Statement
# Help us code this EmailRangesHistory component by implementing the main method. This method should take a String as input and must return a sorted and compacted history with no spaces.
# A single range has the shape of A:B where A and B are numbers and A <= B always.
# The input will contain multiple ranges which are not sorted.
# Each range will be comma separated and there may spaces between the commas.
# 
# These are examples:
# Example 1:
# Input: 1:4  ,  5:10,11:20
# Output: 1:20
# Example 2:
# Input: 5:10,1:2
# Output: 1:2,5:10


def emailRangesHistory(ranges):
    """Returns a simplified range of email history a user has crawled through.

    >>>emailRangesHistory("5:10,1:2")
    >>>1:2, 5:10

    >>>emailRangesHistory("1:4  ,  5:10,11:20")
    >>>1:20
    """
    initial_range = ranges.split(",")
    cleaned_range = [r.strip() for r in initial_range]

    tup_range = [tuple(i.split(":")) for i in cleaned_range]
    # converting to type integer to sort correctly
    integer_range = [(int(i), int(j)) for i, j in tup_range]

    integer_range.sort()
    result = [integer_range[0]]
    current_start = integer_range[0][0]
    current_stop = integer_range[0][1]

    for start, stop in integer_range:
        if start - current_stop > 1:
            # this segment starts after the last segment stops
            # just add a new segment
            result.append((start, stop))
            current_start, current_stop = start, stop
        else:
            # find which overlap range ends at a later number and choose the one that is higher in value
            current_stop = max(current_stop, stop)
            result[-1] = (current_start, current_stop)
            # current_start already guaranteed to be lower

    result = [str(i) for i in result]

    result = [i.replace(", ", ":").strip("()") for i in result]

    final_result = ", ".join(result)
    print final_result
    return final_result

emailRangesHistory("1:4,  22:23,40:49, 42:44,12:15,  5:10, 11:20")
