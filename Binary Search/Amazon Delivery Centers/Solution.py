def calculateDistance(warehouse, centers):
    return 2 * sum(abs(warehouse - center) for center in centers)

def binary_search(centers, l, r, d, search_left):
    ans = None
    while l <= r:
        mid = l + (r - l) // 2
        distance = calculateDistance(mid, centers)
        print(l, r, distance, mid, distance <= d)
        if distance <= d:
            ans = mid  # This mid is a potential answer
            if search_left:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if search_left:
                l = mid + 1
            else:
                r = mid - 1
    return ans

def binarySearch(centers, d):
    left_bound, right_bound = -1e9, 1e9
    print(sorted(centers))
    left = binary_search(centers, left_bound, right_bound, d, True)
    right = binary_search(centers, left_bound, right_bound, d, False)

    print(left, right)
    if left is None and right is None:
        return 0

    return right - left + 1

# Test cases
# print(binarySearch([2, 0, 3, -4], 22) == 5)  # True
# print(binarySearch([-2, 1, 0], 8) == 3)  # True
# print(binarySearch([-3, 2, 2], 8) == 0)  # True
print(binarySearch([2133, 2654, -4807, 1869, -1113, 2547, 4054, 4498, -3265, 3630, -140, -57, 3103, 1778, -726, 1910, 3970, 3589, 4842, 2368, -573, -1080, -2999, -4313, -863, 2074, 4802, 1313, 3787, -3940, 2280, -3967, -1188, -2708, -1863, -2315, 3795, 2658, 3510, -4421, 2023, -1909, 61, -57, -3245, -1271, 456, -600, -546, 74, -3830, -4757, -2072, -754, -2152, -2258, -3358, -2096, -4986, -2269, -2577, -800, 2325, 149, 1820, 3956, 2968, -105, 2689, 2981, -3335, 3769, 3752, 2979, -2776, 4664, -4899, 1249, -4192, -1567, 3814, -889, 4525, -3776, -441, -3349, -3187, 4736, -19, -4643, 786, 3820, 4348, -4598, 2266, 4450, -1128, 3716, 4259, 3964], 525008))
