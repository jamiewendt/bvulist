class bvulist(list):
    def prepend(self, x):
        self.insert(0, x)

    def pop_front(self):
        x = self[0]
        del self[0]
        return x

    def pop_back(self):
        return self.pop()

if __name__ == '__main__':
    L = bvulist()
    L.append(2)
    L.append(3)
    L.prepend(1)
    L.prepend(0)
    print(L)

    L.pop_front()
    L.pop_back()
    print(L)
