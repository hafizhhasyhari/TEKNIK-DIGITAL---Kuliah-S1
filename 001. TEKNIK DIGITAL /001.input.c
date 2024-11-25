#include "input.h"  // Header file input, berisi definisi dan deklarasi terkait input.
#include "ADC.h"    // Header file untuk pengaturan ADC (Analog to Digital Converter).
#include "UART.h"   // Header file untuk pengaturan UART (serial communication).
#include <avr/io.h> // Library untuk kontrol I/O pada mikrokontroler AVR.
#include <stdio.h>  // Library standar untuk input/output.
#include <stdlib.h> // Library standar untuk fungsi alokasi memori dan lainnya.
#include <string.h> // Library standar untuk manipulasi string.

int input_makePacket(UARTPacket* returnData, char* packet) {
    // Fungsi ini memproses paket data dari input UART dan mengisinya ke struktur returnData.
    // Mengembalikan -1 jika ada kesalahan format pada paket, atau 1 jika berhasil.

    if (packet[0] != 0x55 || packet[1] != 0xAA) {
        // Memeriksa apakah paket memiliki header yang benar (0x55 0xAA).
        return -1; // Header salah, fungsi keluar dengan nilai -1.
    }

    if (packet[4] == GENERATOR) {
        // Jika tipe paket adalah GENERATOR (diidentifikasi oleh byte ke-4).
        if (packet[7] != 0x00 || packet[8] != 0x00) {
            // Memeriksa validitas byte ke-7 dan ke-8 (harus 0x00 untuk tipe ini).
            return -1; // Format paket salah.
        }
        returnData->type = packet[4]; // Menyimpan tipe paket.
        returnData->data = (char*)calloc(2, sizeof(char)); 
        // Mengalokasikan memori untuk data (2 byte).
        returnData->data[0] = packet[5]; // Data byte pertama.
        returnData->data[1] = packet[6]; // Data byte kedua.
    } 
    else if (packet[4] == OSCILLOSCOPE) {
        // Jika tipe paket adalah OSCILLOSCOPE.
        if (packet[9] != 0x00 || packet[10] != 0x00) {
            // Memeriksa validitas byte ke-9 dan ke-10 (harus 0x00 untuk tipe ini).
            return -1; // Format paket salah.
        }
        returnData->type = packet[4]; // Menyimpan tipe paket.
        returnData->data = (char*)calloc(4, sizeof(char)); 
        // Mengalokasikan memori untuk data (4 byte).

        // Menghitung sample rate dari byte ke-5 dan ke-6.
        int inputSampleRate = ((packet[5] << 8) & 0x7F00) + packet[6];
        if (inputSampleRate < 10) {
            sampleRate = 24999; // Nilai default jika sample rate terlalu kecil.
        } else if (inputSampleRate > 10000) {
            sampleRate = 24; // Nilai default jika sample rate terlalu besar.
        } else {
            // Perhitungan sample rate sesuai formula tertentu.
            sampleRate = (unsigned long)((16000000.f * (1.f / (float)inputSampleRate) - 64.f) / 64.f);    
        }

        OCR1B = sampleRate; // Mengatur register hardware untuk sample rate.
        OCR1A = sampleRate;

        // Reset buffer ADC untuk kernel dan user.
        ADCBufferIndex[UARTKernel][0] = 0;
        ADCBufferIndex[UARTUser][0] = 0;

        // Menghitung panjang rekaman dari byte ke-7 dan ke-8.
        int inputRecordLength = ((packet[7] << 8) & 0x7F00) + packet[8];
        if (inputRecordLength > 10000) {
            recordLength = 10000; // Maksimum panjang rekaman.
        } else if (inputRecordLength < 10) {
            recordLength = 10; // Minimum panjang rekaman.
        } else {
            recordLength = inputRecordLength; // Panjang rekaman valid.
        }
    } 
    else if (packet[4] == BODEPLOT) {
        // Placeholder untuk tipe paket BODEPLOT (belum diimplementasikan).
    }

    return 1; // Paket berhasil diproses.
}
