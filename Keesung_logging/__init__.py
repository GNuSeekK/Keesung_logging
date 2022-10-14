# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:04:31 2022
v0.0.5 - 배포 가능 첫 버전
v0.0.6 - 경로 확인 추가

@author: 이기성
"""
# version 0.0.6

import logging
import os
import datetime as dt
import shutil


time_text = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
time_set = [dt.datetime.now() - dt.timedelta(days=x) for x in range(0,5)]
time_set = set([x.strftime('%Y%m%d') for x in time_set])


class my_logger:
    
    def __init__(self, file_name = 'root', save_path = os.path.dirname(os.path.abspath(__file__))):
        # info 로그 생성
        path = os.path.join(save_path, 'log', time_text.split('_')[0])
        
        # 오늘 폴더 만들기
        if not os.path.exists(path):
            os.makedirs(path)
            
        # 5일전 폴더까지 삭제
        folder_list = os.listdir(os.path.join(save_path, 'log'))
        for folder in folder_list:
            if folder not in time_set:
                shutil.rmtree(os.path.join(save_path, 'log', folder))
                
        if file_name == 'root':
            rootname = ''
        else:
            rootname = file_name
        self.logger = logging.getLogger(f'{rootname}')
        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] >> %(message)s')
        # 로그 출력
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)
        # 로그 파일에 출력
        self.root_path = os.path.join(path, f'{file_name}_{time_text}.log')
        self.file_handler = logging.FileHandler(self.root_path)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
    
        # error 로그 생성
        self.error_logger = logging.getLogger('error')
        self.error_logger.handlers.clear()
        self.error_logger.setLevel(logging.ERROR)
        self.error_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] >> %(message)s')
        # 에러 로그 파일에 출력
        self.error_path = os.path.join(path, f'error_{time_text}.log')
        self.error_file_handler = logging.FileHandler(self.error_path)
        self.error_file_handler.setFormatter(self.error_formatter)
        self.error_logger.addHandler(self.error_file_handler)
        
    def info(self, txt):
        self.logger.info(txt)
        
    def error(self, txt):
        self.error_logger.error(txt)
        print(f'{self.error_path}를 확인해주세요')