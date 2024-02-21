#include <iostream>
#include <queue>
using namespace std;

struct Node
{
    int y, x;
};

int dy[] = { 1, 0, -1, 0 };
int dx[] = { 0, 1, 0,-1 };
int T;
int N, W, H;
int graph[15][13];
int dat[4][15][12];
int boomed[15][12];
int cnt_min = 0;

void Init()
{
    cnt_min = 213456789;
}

void Input()
{
    cin >> N >> W >> H;
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            cin >> graph[y][x];
        }
    }
}

void DfsShoot(int n)
{
    if (n == N)
    {
        return;
    }
}

void Gravity()
{
    // segmentation error 발생
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            if (boomed[y][x] == 1)
            {
                graph[y][x] = 0;
            }
        }
    }
    for (int x = 0; x < W; x++)
    {
        queue<int> col;
        for (int y = H - 1; y >= 0; y--)
        {
            if (graph[y][x] != 0)
            {
                col.push(graph[y][x]);
            }
        }
        // 열 초기화
        for (int y = H - 1; y >= 0; y--)
        {
            graph[y][x] = 0;
        }
        // 큐에 저장된 배열 채워넣기
        int y = H - 1;
        while (!col.empty())
        {
            graph[y][x] = col.front();
            col.pop();
            y--;
        }
    }
}

void InitBoom()
{
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            boomed[y][x] = 0;
        }
    }
}

void Boom(int x_tar)
{
    InitBoom();
    // x인 좌표에서 0이 아닌 지점 찾기
    int y_tar = 0;
    while (true)
    {
        if (graph[y_tar][x_tar] != 0)
        {
            break;
        }
        y_tar++;
    }
    if (y_tar >= H) // 벽돌이 비어있는 경우
    {
        return;
    }
    queue<Node> q;
    q.push({ y_tar, x_tar });
    boomed[y_tar][x_tar] = 1;
    while (!q.empty())
    {
        Node current = q.front();
        q.pop();
        int boom_power = graph[current.y][current.x] - 1;
        if (boom_power == 0)
        {
            continue;
        }
        for (int i = 1; i <= boom_power; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                int ny = current.y + dy[j] * i;
                int nx = current.x + dx[j] * i;
                if (ny >= H || nx >= W || ny < 0 || nx < 0)
                {
                    continue;
                }
                if (graph[ny][nx] == 0)
                {
                    continue;
                }
                if (boomed[ny][nx] == 1)
                {
                    continue;
                }
                boomed[ny][nx] = 1;
                q.push({ ny, nx });
            }
        }
    }

    // 내려앉기
    Gravity();
}

void GraphToDat(int n) // 현재의 그래프를 Dat n에 저장
{
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            dat[n][y][x] = graph[y][x];
        }
    }
}

void DatToGraph(int n) // Dat n 그래프를 현재의 그래프에 적용
{
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            graph[y][x] = dat[n][y][x];
        }
    }
}

int CntBricks()
{
    int cnt_bricks = 0;
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            if (graph[y][x] != 0)
            {
                cnt_bricks++;
            }
        }
    }
    return cnt_bricks;
}

void Dfs(int level)
{
    if (level == N)
    {
        int cnt_current = CntBricks();
        if (cnt_current < cnt_min)
        {
            cnt_min = cnt_current;
        }
        return; // 남은 벽돌 세야함
    }
    for (int x = 0; x < W; x++)
    {
        GraphToDat(level);
        Boom(x); // x열에 폭탄 떨어뜨리기
        // 폭탄 맞은 상황
        Dfs(level + 1);
        // 폭탄 맞은 거 복구하기
        DatToGraph(level);
    }
}

int main()
{
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        Init();
        Input();
        Dfs(0);
        cout << "#" << test_case << " " << cnt_min << "\n";
    }
    return 0;
}