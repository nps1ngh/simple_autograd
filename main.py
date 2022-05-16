import numpy as np
import torch

from simple_autograd import Variable


def main1():
    x = np.ones(3) * 3
    print(f"{x=}")
    x = Variable(x)
    print(f"{x=}")

    y = np.ones((4, 3)) - x
    y.retain_grad()
    print(f"{y=}")

    z = (y * np.array([2, 2, 2], dtype=float)).sum()
    z.retain_grad()
    print(f"{z=}")

    z.backward()
    print(f"{x.grad=}")
    print(f"{y.grad=}")
    print(f"{z.grad=}")


def main2():
    x = np.arange(3, 6).reshape(-1, 1) * np.arange(1, 4)
    x = np.asarray(x, float)
    x = Variable(x, requires_grad=True)
    print(f"{x=}")

    y = np.array([0, 1, 0]) * x
    y.retain_grad()
    print(y)

    z = y.max(1, keepdims=True)
    z.retain_grad()
    print(z)

    u = np.array([0, 1, 0]) * z
    u.retain_grad()
    print(u)
    t = u.mean()
    t.retain_grad()
    print(t)
    t.backward()

    print(f"{x.grad=}")
    print(f"{z.grad=}")
    print(f"{y.grad=}")
    print("Now torch")
    x = torch.arange(3, 6).reshape(-1, 1) * torch.arange(1, 4)
    x = x.float()
    x.requires_grad = True
    print(f"{x=}")

    y = torch.tensor([0, 1, 0]) * x
    y.retain_grad()
    print(y)

    z = y.max(1, keepdims=True).values
    z.retain_grad()
    print(z)

    u = torch.tensor([0, 1, 0]) * z
    print(u)
    t = u.mean()
    print(t)
    t.backward()

    print(f"{x.grad=}")
    print(f"{z.grad=}")
    print(f"{y.grad=}")


def main3():
    x = np.ones((3, 4))
    print(f"{x=}")
    x = Variable(x, requires_grad=True)
    print(f"{x=}")
    y = x[[0, 0]]
    y.retain_grad()
    print(f"{y=}")
    z = y.sum()
    z.retain_grad()
    print(f"{z=}")
    z.backward()

    print(f"{x.grad=}")
    print(f"{y.grad=}")
    print(f"{z.grad=}")

    x = torch.ones(3, 4, requires_grad=True)
    print(f"{x=}")
    y = x[[0, 0]]
    y.retain_grad()
    print(f"{y=}")
    z = y.sum()
    z.retain_grad()
    print(f"{z=}")
    z.backward()

    print(f"{x.grad=}")
    print(f"{y.grad=}")
    print(f"{z.grad=}")


if __name__ == '__main__':
    main3()
    main1()
    main2()
