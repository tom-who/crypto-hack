#include <stdio.h>
#include <stdint.h>

int main(){
    int nums[] = {99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125};
    for (int i = 0; i < sizeof(nums) / sizeof(nums[0]); i++){
        printf("%c", (char)nums[i]);
    }
    printf("\n");
}
