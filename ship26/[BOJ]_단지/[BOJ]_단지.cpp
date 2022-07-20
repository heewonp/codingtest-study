#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


int Countarray(int arr[][30], int i, int j, int Max, int* count);

int main(int arg, char** argv)
{
	int count = 0;  //카운트 변수. 
	std::vector<int> countarr;  // 카운트를 담을 벡터
	int Max;  //배열의 크기 변수
	std::string buffer; //STRING 버퍼
	std::cin >> Max;  //배열의 크기를 받는다.
	int Value = 0;

	// 2차원 배열 생성  5 <= N <= 25 인 배열 이므로 크기가 30인 배열을 쓸거임.전부 0으로 초기화.
	int arr[30][30] = {
		{0,}
	};

	std::cin.ignore();  // 개행 문자 제거
	for (int i = 0; i < Max; i++)  //MAX값동안
	{

		getline(std::cin, buffer);  //한줄을 받는다


		for (int j = 0; j < buffer.size(); j++)
		{
			arr[i][j] = int(buffer[j] - '0');  //배열 채워넣기.
		}


	}







	for (int i = 0; i < Max; i++)   //배열돌면서 재귀호출
	{
		for (int j = 0; j < Max; j++)
		{

			Value = Countarray(arr, i, j, Max, &count);
			count = 0; //초기화
			if (Value > 0)
			{
				countarr.push_back(Value);
				Value = 0;
			}


		}


	}


	std::cout << countarr.size() << '\n';
	std::vector<int>::iterator iter;
	std::sort(countarr.begin(), countarr.end());
	for (iter = countarr.begin(); iter != countarr.end(); iter++)
	{
		std::cout << *iter << std::endl;
	}




}


int Countarray(int arr[][30], int i, int j, int Max, int* count)  //Recursive Function
{


	if (arr[i][j] == 1)
	{
		arr[i][j] = 0;
		*count += 1;  //네모칸이 1이면 0으로 바꾸고 카운트를 증가 시킬 거시다.

		if (i > 0)  //만약 위에칸이 인덱스를벗어나지않으면
		{

			if (i < (Max - 1))  //만약 아래 칸이 인덱스를 벗어나지 않으면  (위아래로 칸이존재)
			{
				if (arr[i - 1][j] == 1 && arr[i + 1][j] == 0)
				{
					Countarray(arr, (i - 1), j, Max, count);   //위에칸확인
				}
				else if (arr[i + 1][j] == 1 && arr[i - 1][j] == 0)
				{
					Countarray(arr, (i + 1), j, Max, count);  //아래칸확인
				}
				else
				{
					Countarray(arr, (i - 1), j, Max, count);   //위에칸확인
					Countarray(arr, (i + 1), j, Max, count);  //아래칸확인
				}
				if (j > 0)  //왼쪽칸을 갈 수 있을 경우
				{

					if (j < (Max - 1)) //양옆으로 칸이존재할 경우
					{
						if (arr[i][j - 1] == 1 && arr[i][j + 1] == 0)
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
						}
						else if (arr[i][j + 1] == 1 && arr[i][j - 1] == 0)
						{
							Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
						}
						else
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
							Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
						}

					}
					else //왼쪽만 갈 수 있는 경우
					{
						if (arr[i][j - 1] == 1)
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
						}
					}



				}
				else  //왼쪽 칸을 갈 수 없는경우
				{
					if (arr[i][j + 1] == 1)
					{
						Countarray(arr, i, (j + 1), Max, count);   //오른쪽칸확인
					}

				}



			}
			else  //위에칸은 갈수 있고 아래칸이 막힌경우
			{

				if (arr[i - 1][j] == 1)
				{
					Countarray(arr, (i - 1), j, Max, count);   //위에칸확인
				}
				if (j > 0)  //왼쪽칸을 갈 수 있을 경우
				{

					if (j < (Max - 1)) //양옆으로 칸이존재할 경우
					{
						if (arr[i][j - 1] == 1 && arr[i][j + 1] == 0)
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
						}
						else if (arr[i][j + 1] == 1 && arr[i][j - 1] == 0)
						{
							Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
						}
						else
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
							Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
						}

					}
					else //왼쪽만 갈 수 있는 경우
					{
						if (arr[i][j - 1] == 1)
						{
							Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
						}
					}



				}
				else  //왼쪽 칸을 갈 수 없는경우
				{
					if (arr[i][j + 1] == 1)
					{
						Countarray(arr, i, (j + 1), Max, count);   //오른쪽칸확인
					}

				}



			}

		}
		else  //위에칸이 막힌경우
		{

			if (arr[i + 1][j] == 1)
			{
				Countarray(arr, (i + 1), j, Max, count);   //아래칸확인
			}


			if (j > 0)  //왼쪽칸을 갈 수 있을 경우
			{

				if (j < (Max - 1)) //양옆으로 칸이존재할 경우
				{
					if (arr[i][j - 1] == 1 && arr[i][j + 1] == 0)
					{
						Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
					}
					else if (arr[i][j + 1] == 1 && arr[i][j - 1] == 0)
					{
						Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
					}
					else
					{
						Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
						Countarray(arr, i, (j + 1), Max, count);  //오른쪽칸확인
					}

				}
				else //왼쪽만 갈 수 있는 경우
				{
					if (arr[i][j - 1] == 1)
					{
						Countarray(arr, i, (j - 1), Max, count);   //왼쪽칸확인
					}
				}



			}
			else  //왼쪽 칸을 갈 수 없는경우
			{
				if (arr[i][j + 1] == 1)
				{
					Countarray(arr, i, (j + 1), Max, count);   //오른쪽칸확인
				}

			}

		}

	}

	return *count;  //count의 값을 반환할 거시다.
}

