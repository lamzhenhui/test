package main

import (
	"errors"
	"github.com/golang/mock/gomock"
	"testing"
)

func TestGetFromDB(t *testing.T) {

	ctrl := gomock.NewController(t)
	defer ctrl.Finish() // 断言 DB.Get() 方法是否被调用


	m := NewMockDB(ctrl)
	m.EXPECT().Get(gomock.Eq("Tom")).Return(100, errors.New("not exist"))

	if v := GetFromDB(m, "Tom"); v != -1 {
		t.Fatal("expected -1, but got", v)
	}
}

func TestGetFromDB1(t *testing.T) {
	type args struct {
		db  DB
		key string
	}
	type fields_ struct {
		node_ser *MockNodeService
	}
	ctrl := gomock.NewController(t)
	defer ctrl.Finish() // 断言 DB.Get() 方法是否被调用


	m := NewMockDB(ctrl)
	m.EXPECT().Get(gomock.Eq("Tom")).Return(100, errors.New("not exist"))

	m2 := NewMockNodeService(ctrl)
	m2.EXPECT().FindAllNodeDefines().Return(1,nil, errors.New("not exist"))
	tests := []struct {
		name string
		fields fields_
		args args
		want int
	}{{
		"name",
		fields_{},
		args{m,"Tom"},
		-1,
	},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetFromDB(tt.args.db, tt.args.key); got != tt.want {
				t.Errorf("GetFromDB() = %v, want %v", got, tt.want)
			}

		})
	}
}